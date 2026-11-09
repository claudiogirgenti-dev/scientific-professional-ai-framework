# Compatibilità delle piattaforme

## Principio

Le skill sono mantenute nel formato Agent Skills (`SKILL.md`) in `.agents/skills/`. Le definizioni canoniche degli agenti sono mantenute in `agents/`, mentre ogni piattaforma riceve un adattatore dedicato.

## Antigravity

- Istruzioni comuni: `AGENTS.md` alla radice e `.agents/AGENTS.md`.
- Agenti: `.agents/agents/<nome>.md`.
- Skill: `.agents/skills/<nome-skill>/SKILL.md`.

Documentazione ufficiale:
- https://antigravity.google/docs/customization-discovery/
- https://antigravity.google/docs/skills/
- https://www.antigravity.google/docs/cli/commands/agents/

## OpenAI Codex

- Istruzioni comuni: `AGENTS.md` alla radice del repository.
- Agenti personalizzati: `.codex/agents/<nome>.toml`.
- Skill: `.agents/skills/<nome-skill>/SKILL.md`.

Documentazione ufficiale:
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/build-skills

## Standard Agent Skills

Ogni skill è una cartella che contiene almeno `SKILL.md`, con frontmatter YAML obbligatorio (`name` e `description`) e istruzioni Markdown. Questo repository mantiene le skill esclusivamente testuali, come richiesto dall'impostazione del framework.

## Limiti e verifiche

Il supporto e il comportamento possono cambiare tra versioni delle piattaforme. Prima di distribuire un aggiornamento, verificare la documentazione ufficiale. Gli agenti personalizzati potrebbero richiedere attivazione esplicita o delega da parte dell'agente principale. Nessun adattatore può garantire accesso a strumenti non concessi dall'ambiente.

## Claude Code

- Istruzioni comuni: `CLAUDE.md` alla radice; richiama `AGENTS.md`.
- Subagenti: `.claude/agents/<nome>.md`.
- Nel repository del framework, le skill canoniche sono in `.agents/skills/<nome-skill>/SKILL.md`.
- Nell'installazione per un progetto Claude Code, l'installatore le copia in `.claude/skills/<nome-skill>/SKILL.md`.

Documentazione di riferimento:
- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
- https://platform.claude.com/docs/en/managed-agents/skills

## GitHub Copilot

- Istruzioni comuni: `.github/copilot-instructions.md`, che richiama `AGENTS.md`.
- Agenti: `.github/agents/<nome>.agent.md`.
- Skill: `.agents/skills/<nome-skill>/SKILL.md`, percorso riconosciuto da Copilot.
- L'installazione selettiva `--platform copilot` usa la posizione nativa `.github/skills/` nel progetto di destinazione.

Documentazione ufficiale:
- https://docs.github.com/en/copilot/reference/customization-cheat-sheet
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills

## Distribuzione

L'installatore supporta `--platform all` (predefinito), `both` (Antigravity e Codex), `antigravity`, `codex`, `claude` e `copilot`. Il repository del framework mantiene una sola copia canonica per skill in `.agents/skills/`: non aggiungere copie con gli stessi nomi in `.claude/skills/` o `.github/skills/`, perché gli importatori possono rilevarle come duplicati. L'installatore genera la copia nella posizione nativa richiesta nel progetto di destinazione.
