# Adattatori di piattaforma

## Antigravity

Le definizioni Markdown sono distribuite in `.agents/agents/`; le skill condivise sono in `.agents/skills/`. Le istruzioni comuni sono in `AGENTS.md` e `.agents/AGENTS.md`.

## Codex

Le definizioni TOML sono distribuite in `.codex/agents/`; le skill condivise restano in `.agents/skills/`. Le istruzioni principali sono in `AGENTS.md` alla radice del progetto.

## Regola di manutenzione

Modificare prima la definizione canonica in `agents/`. Poi aggiornare le copie specifiche nelle directory dell'adattatore. Eseguire `python tools/validate_repository.py` dopo ogni modifica.

Gli adattatori descrivono ruoli e istruzioni, ma la selezione, delega e concorrenza dipendono dall'orchestratore della piattaforma.

## Claude Code

Agenti in `.claude/agents/`, skill in `.claude/skills/`, istruzioni di progetto in `CLAUDE.md`.

## GitHub Copilot

Agenti in `.github/agents/`, skill in `.github/skills/`, istruzioni in `.github/copilot-instructions.md`.
