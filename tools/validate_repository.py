#!/usr/bin/env python3
"""Controlli strutturali locali del repository; usa solo la libreria standard."""
from pathlib import Path
import re
import sys
try:
    import tomllib
except ModuleNotFoundError:
    tomllib = None

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ["coordinatore", "interlocutore", "curioso", "critico", "professore", "consigliere", "bilancia", "spia", "sintetizzatore"]
errors = []

for rel in ["README.md", "AGENTS.md", ".agents/AGENTS.md", "CLAUDE.md", ".github/copilot-instructions.md", "docs/ARCHITETTURA.md", "docs/PROTOCOLLO_OPERATIVO.md", "docs/GOVERNANCE_E_AUTORIZZAZIONI.md", "templates/PROJECT_SYNTHESIS.md", "tools/install_framework.py"]:
    if not (ROOT / rel).is_file():
        errors.append(f"File richiesto mancante: {rel}")

for name in AGENTS:
    canonical = ROOT / "agents" / f"{name}.md"
    ant = ROOT / ".agents" / "agents" / f"{name}.md"
    codex = ROOT / ".codex" / "agents" / f"{name}.toml"
    claude = ROOT / ".claude" / "agents" / f"{name}.md"
    copilot = ROOT / ".github" / "agents" / f"{name}.agent.md"
    for p in (canonical, ant, codex, claude, copilot):
        if not p.is_file():
            errors.append(f"Definizione agente mancante: {p.relative_to(ROOT)}")
    if codex.is_file() and tomllib:
        try:
            data = tomllib.loads(codex.read_text(encoding="utf-8"))
            for key in ("name", "description", "developer_instructions"):
                if not data.get(key):
                    errors.append(f"Campo TOML mancante in {codex.relative_to(ROOT)}: {key}")
        except Exception as exc:
            errors.append(f"TOML non valido {codex.relative_to(ROOT)}: {exc}")

skills_dir = ROOT / ".agents" / "skills"
skill_locations = {}
for rel_root in (".agents/skills", ".claude/skills", ".github/skills"):
    skill_root = ROOT / rel_root
    if not skill_root.is_dir():
        continue
    for folder in sorted(p for p in skill_root.iterdir() if p.is_dir()):
        skill_file = folder / "SKILL.md"
        if not skill_file.is_file():
            continue
        content = skill_file.read_text(encoding="utf-8")
        match = re.search(r"(?m)^name:\s*([^\s#]+)\s*(?:#.*)?$", content[:500])
        if match:
            skill_locations.setdefault(match.group(1), []).append(
                skill_file.relative_to(ROOT).as_posix()
            )

for name, locations in sorted(skill_locations.items()):
    if len(locations) > 1:
        errors.append(f"Skill duplicata '{name}': " + ", ".join(locations))

for folder in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
    skill_file = folder / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"SKILL.md mancante: {folder.relative_to(ROOT)}")
        continue
    content = skill_file.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        errors.append(f"Frontmatter YAML mancante: {skill_file.relative_to(ROOT)}")
    if "\nname: " not in content[:500] or "\ndescription: " not in content[:1000]:
        errors.append(f"Metadati name/description mancanti: {skill_file.relative_to(ROOT)}")
    expected_name = folder.name
    if f"\nname: {expected_name}\n" not in content[:500]:
        errors.append(f"Nome skill non coerente con la cartella: {skill_file.relative_to(ROOT)}")

if errors:
    print("VALIDAZIONE FALLITA")
    for error in errors:
        print("- " + error)
    raise SystemExit(1)

print(f"VALIDAZIONE OK: {len(AGENTS)} agenti e {len(list(skills_dir.iterdir()))} skill rilevati.")

if not tomllib:
    print("ATTENZIONE: Python < 3.11; controllo sintattico TOML non eseguito.")
