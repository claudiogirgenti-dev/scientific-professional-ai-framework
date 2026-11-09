# Scientific & Professional AI Framework

**Framework modulare di agenti e competenze per progetti scientifici, tecnici e professionali**  
Versione iniziale: `0.1.0` · Lingua: italiano

## Che cos'è

Questo repository contiene un insieme riutilizzabile di agenti AI, skill universali e protocolli di lavoro. È progettato per essere installato integralmente o in modo selettivo nei singoli progetti e per essere adattato a più ambienti AI.

Il framework non è un'applicazione autonoma né un motore multi-agente indipendente: fornisce istruzioni e configurazioni che l'ambiente AI deve interpretare. L'effettiva delega agli agenti, l'accesso agli strumenti e l'esecuzione parallela dipendono dalle capacità e dai permessi della piattaforma utilizzata.

## Componenti

- **9 agenti:** Coordinatore, Interlocutore, Curioso, Critico, Professore, Consigliere, Bilancia, Spia e Sintetizzatore.
- **Skill universali:** procedure testuali condivise e riutilizzabili da tutti gli agenti.
- **Protocolli centrali:** frazionamento dei comandi, gestione delle decisioni, controllo qualità, autorizzazioni e continuità del progetto.
- **Adattatori:** configurazioni per Antigravity, Codex, Claude Code e GitHub Copilot.
- **Strumenti di supporto:** installazione selettiva e validazione strutturale del repository (non sono skill e non vengono eseguiti automaticamente dagli agenti).

## Struttura

```text
scientific-professional-ai-framework/
├── AGENTS.md                      # Istruzioni comuni per l'agente principale
├── .agents/
│   ├── AGENTS.md                  # Istruzioni workspace per Antigravity
│   ├── agents/                    # Agenti Markdown per Antigravity
│   └── skills/                    # Skill Agent Skills, condivise
├── .codex/agents/                 # Agenti Codex in TOML
├── .claude/agents/                # Subagenti Claude Code in Markdown
├── .github/agents/                # Agenti GitHub Copilot
├── agents/                        # Definizioni canoniche degli agenti
├── docs/                          # Architettura, governance, installazione
├── templates/PROJECT_SYNTHESIS.md # Modello della memoria di progetto
└── tools/                         # Installatore e validatore del repository
```

Nel repository del framework le skill sono mantenute una sola volta in `.agents/skills/`, percorso condiviso da Antigravity, Codex e GitHub Copilot. L'installatore le copia nella posizione nativa della piattaforma scelta nel progetto di destinazione.

## Installazione rapida

1. Creare un repository GitHub vuoto.
2. Estrarre lo ZIP sul computer e caricare nel repository **il contenuto della cartella** `scientific-professional-ai-framework` (non il file ZIP come singolo file), mantenendo anche le cartelle nascoste che iniziano con il punto.
3. Clonare o scaricare il repository nel computer in cui si trova il progetto di destinazione.
4. Aprire un terminale nella cartella del framework.
5. Eseguire l'installazione completa:

```bash
python tools/install_framework.py --target "PERCORSO_DEL_PROGETTO" --all
```

L'opzione `--all` installa tutti i nove agenti, le diciotto skill e, per impostazione predefinita, i quattro adattatori disponibili.

Per installare soltanto alcuni agenti e skill:

```bash
python tools/install_framework.py --target "PERCORSO_DEL_PROGETTO" \
  --agents coordinatore,interlocutore,professore,critico \
  --skills avvio-progetto-e-obiettivi,ricerca-e-verifica-fonti,controllo-qualita
```

L'installatore include automaticamente Coordinatore e Sintetizzatore quando viene selezionato almeno un agente, perché sono necessari alla governance e alla memoria condivisa. È possibile scegliere l'ambiente:

```bash
python tools/install_framework.py --target "PERCORSO_DEL_PROGETTO" --all --platform antigravity
python tools/install_framework.py --target "PERCORSO_DEL_PROGETTO" --all --platform codex
python tools/install_framework.py --target "PERCORSO_DEL_PROGETTO" --all --platform claude
python tools/install_framework.py --target "PERCORSO_DEL_PROGETTO" --all --platform copilot
```

L'installazione non sovrascrive file già esistenti per impostazione predefinita. Per sostituire file presenti dopo averne verificato le differenze, usare esplicitamente `--overwrite`.

## Regole fondamentali

1. Il progetto inizia dalla comprensione dell'idea e dalla definizione condivisa di obiettivi, risultati attesi e criteri di completamento.
2. Non iniziare a modificare codice o file del progetto quando requisiti e autorizzazioni non sono sufficientemente chiari.
3. Gli agenti ricevono il contesto comune; intervengono attivamente solo quando il tema è pertinente al proprio ruolo.
4. Nelle fasi iniziali di un progetto il Coordinatore consulta tutti gli agenti disponibili; le valutazioni sono indipendenti e, quando possibile, parallele. Negli step successivi seleziona gli agenti pertinenti e motiva le esclusioni non ovvie. Gli agenti non svolgono dibattiti diretti tra loro.
5. Il Coordinatore controlla ogni contributo prima che venga utilizzato.
6. Il Sintetizzatore è l'unico agente autorizzato a modificare `PROJECT_SYNTHESIS.md`.
7. Prima di ogni nuovo step gli agenti leggono `PROJECT_SYNTHESIS.md`; alla fine di ogni step completato il Sintetizzatore lo aggiorna.
8. Le divergenze tra agenti devono essere mostrate, non cancellate o risolte artificialmente.
9. Le operazioni preparatorie sono autonome; le modifiche sostanziali al progetto, al codice scientifico e agli obiettivi richiedono autorizzazione.
10. Il controllo scientifico deve distinguere la correttezza scientifica dalla scelta operativa consapevole dell'utente.

## Verifica del repository

Dalla cartella principale:

```bash
python tools/validate_repository.py
```

Lo script verifica la presenza dei file, i metadati minimi delle skill e la struttura TOML degli agenti Codex. Non verifica il comportamento effettivo dei modelli AI.

## Compatibilità e limiti

Le skill sono basate sul formato aperto `SKILL.md` e mantenute in `.agents/skills/`. Le definizioni degli agenti sono adattate separatamente: Markdown per Antigravity e TOML per Codex.

Il framework non può garantire che ogni piattaforma attivi automaticamente tutti gli agenti, esegua processi in parallelo o disponga degli stessi strumenti. Il Coordinatore deve verificare le capacità disponibili, consultare solo gli agenti effettivamente accessibili e dichiarare eventuali limiti o incarichi non eseguibili.

Vedere:
- `docs/ARCHITETTURA.md`
- `docs/PROTOCOLLO_OPERATIVO.md`
- `docs/GOVERNANCE_E_AUTORIZZAZIONI.md`
- `docs/INSTALLAZIONE_E_AGGIORNAMENTO.md`
- `docs/COMPATIBILITA.md`

## Licenza

Non è stata inclusa una licenza open source: la scelta dei termini di distribuzione resta a carico del titolare del repository. Prima di rendere pubblico il repository, aggiungere una licenza se si desidera concedere esplicitamente diritti di riutilizzo a terzi.
