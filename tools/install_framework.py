#!/usr/bin/env python3
"""Installa selettivamente agenti e skill in un progetto di destinazione.

Richiede soltanto la libreria standard Python. Non modifica file esistenti
se non viene passato --overwrite. Nessun aggiornamento viene eseguito in background.
"""
from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = [
    "coordinatore", "interlocutore", "curioso", "critico", "professore",
    "consigliere", "bilancia", "spia", "sintetizzatore"
]
SKILLS = sorted(p.name for p in (ROOT / ".agents" / "skills").iterdir() if p.is_dir())
MANDATORY_AGENTS = {"coordinatore", "sintetizzatore"}


def parse_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def copy_file(source: Path, destination: Path, *, overwrite: bool, dry_run: bool, actions: list[str]) -> None:
    if not source.is_file():
        raise FileNotFoundError(f"File sorgente mancante: {source}")
    if destination.exists() and not overwrite:
        actions.append(f"SKIP (già esistente): {destination}")
        return
    actions.append(f"COPIA: {source.relative_to(ROOT)} -> {destination}")
    if not dry_run:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description="Installa agenti e skill del framework in un progetto.")
    parser.add_argument("--target", required=True, help="Cartella radice del progetto di destinazione")
    parser.add_argument("--all", action="store_true", help="Installa tutti gli agenti e tutte le skill")
    parser.add_argument("--agents", help="Elenco agenti separati da virgola")
    parser.add_argument("--skills", help="Elenco skill separati da virgola")
    parser.add_argument("--platform", choices=["all", "both", "antigravity", "codex", "claude", "copilot"], default="all")
    parser.add_argument("--overwrite", action="store_true", help="Sovrascrive i file esistenti (solo dopo verifica e approvazione)")
    parser.add_argument("--dry-run", action="store_true", help="Mostra le operazioni senza copiare file")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    if target == ROOT or ROOT in target.parents:
        print("ERRORE: la destinazione non può essere il repository sorgente o una sua sottocartella.", file=sys.stderr)
        return 2
    if not args.all and not args.agents and not args.skills:
        parser.error("Specificare --all oppure almeno uno tra --agents e --skills.")

    selected_agents = list(AGENTS) if args.all else parse_csv(args.agents)
    selected_skills = list(SKILLS) if args.all else parse_csv(args.skills)

    unknown_agents = sorted(set(selected_agents) - set(AGENTS))
    unknown_skills = sorted(set(selected_skills) - set(SKILLS))
    if unknown_agents or unknown_skills:
        if unknown_agents:
            print("Agenti sconosciuti: " + ", ".join(unknown_agents), file=sys.stderr)
        if unknown_skills:
            print("Skill sconosciute: " + ", ".join(unknown_skills), file=sys.stderr)
        return 2

    if selected_agents:
        selected_agents = sorted(set(selected_agents) | MANDATORY_AGENTS, key=AGENTS.index)

    actions: list[str] = []
    if selected_agents:
        # Istruzioni generali comuni alle piattaforme supportate.
        copy_file(ROOT / "AGENTS.md", target / "AGENTS.md", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)
        platforms = {"all": {"antigravity", "codex", "claude", "copilot"}, "both": {"antigravity", "codex"}}.get(args.platform, {args.platform})
        if "antigravity" in platforms:
            copy_file(ROOT / ".agents" / "AGENTS.md", target / ".agents" / "AGENTS.md", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)
        if "claude" in platforms:
            copy_file(ROOT / "CLAUDE.md", target / "CLAUDE.md", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)
        if "copilot" in platforms:
            copy_file(ROOT / ".github" / "copilot-instructions.md", target / ".github" / "copilot-instructions.md", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)
        # Initialize the per-project memory only if absent.
        copy_file(ROOT / "templates" / "PROJECT_SYNTHESIS.md", target / "PROJECT_SYNTHESIS.md", overwrite=False, dry_run=args.dry_run, actions=actions)

        for agent in selected_agents:
            if "antigravity" in platforms:
                copy_file(ROOT / ".agents" / "agents" / f"{agent}.md", target / ".agents" / "agents" / f"{agent}.md", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)
            if "codex" in platforms:
                copy_file(ROOT / ".codex" / "agents" / f"{agent}.toml", target / ".codex" / "agents" / f"{agent}.toml", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)
            if "claude" in platforms:
                copy_file(ROOT / ".claude" / "agents" / f"{agent}.md", target / ".claude" / "agents" / f"{agent}.md", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)
            if "copilot" in platforms:
                copy_file(ROOT / ".github" / "agents" / f"{agent}.agent.md", target / ".github" / "agents" / f"{agent}.agent.md", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)

    platforms = {"all": {"antigravity", "codex", "claude", "copilot"}, "both": {"antigravity", "codex"}}.get(args.platform, {args.platform})
    for skill in selected_skills:
        source_skill = ROOT / ".agents" / "skills" / skill / "SKILL.md"
        # Antigravity and Codex use the shared .agents/skills location.
        if platforms & {"antigravity", "codex"}:
            copy_file(source_skill, target / ".agents" / "skills" / skill / "SKILL.md", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)
        if "claude" in platforms:
            copy_file(source_skill, target / ".claude" / "skills" / skill / "SKILL.md", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)
        if "copilot" in platforms:
            copy_file(source_skill, target / ".github" / "skills" / skill / "SKILL.md", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)

    copy_file(ROOT / "VERSION", target / ".scientific-ai-framework-version", overwrite=args.overwrite, dry_run=args.dry_run, actions=actions)

    print("\nPiano di installazione" if args.dry_run else "\nOperazioni di installazione")
    print(f"Destinazione: {target}")
    print(f"Piattaforma: {args.platform}")
    print("Agenti: " + (", ".join(selected_agents) if selected_agents else "nessuno"))
    print("Skill: " + (", ".join(selected_skills) if selected_skills else "nessuna"))
    print("\n".join(actions) if actions else "Nessun file da copiare.")
    if args.dry_run:
        print("\nAnteprima completata: nessun file è stato modificato.")
    else:
        print("\nInstallazione terminata. Verificare i file segnalati come SKIP e leggere docs/INSTALLAZIONE_E_AGGIORNAMENTO.md.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
