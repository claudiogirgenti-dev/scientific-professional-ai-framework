# Installazione, selezione e aggiornamento

## 1. Installazione completa

Dalla cartella principale del repository:

```bash
python tools/install_framework.py --target "PERCORSO_PROGETTO" --all
```

Per Windows è possibile usare anche:

```powershell
python .\tools\install_framework.py --target "C:\Percorso\Progetto" --all
```

## 2. Installazione selettiva

```bash
python tools/install_framework.py --target "PERCORSO_PROGETTO" \
  --agents coordinatore,interlocutore,professore,critico \
  --skills avvio-progetto-e-obiettivi,ricerca-e-verifica-fonti,controllo-qualita
```

Coordinatore e Sintetizzatore sono aggiunti automaticamente quando si seleziona almeno un agente.

## 3. Scelta della piattaforma

- `--platform all`: installa Antigravity, Codex, Claude Code e GitHub Copilot (predefinito).
- `--platform both`: installa Antigravity e Codex.
- `--platform antigravity`, `codex`, `claude` o `copilot`: installa un solo adattatore.

Le skill sono copiate nella posizione nativa di ciascuna piattaforma a partire dalla versione canonica in `.agents/skills/`.

## 4. Anteprima

Aggiungere `--dry-run` per visualizzare i file che verrebbero copiati senza scrivere nulla.

## 5. File già esistenti

Per impostazione predefinita l'installatore non sovrascrive file esistenti. Se trova conflitti li segnala e li lascia invariati. Controllare i contenuti prima di decidere se usare `--overwrite`.

Se il progetto contiene già un `AGENTS.md`, non sostituirlo alla cieca: integrare manualmente le istruzioni centrali, mantenendo le regole specifiche del progetto.

## 6. Aggiornamento controllato

1. Consultare il changelog e confrontare la nuova versione del repository centrale con quella attualmente installata.
2. Verificare le differenze nelle definizioni canoniche, negli adattatori e nelle skill.
3. Eseguire prima un'anteprima con `--dry-run`.
4. Ottenere l'approvazione dell'utente per l'intervento di aggiornamento.
5. Applicare con `--overwrite` soltanto dopo l'approvazione.
6. Controllare i file modificati e verificare il comportamento nell'ambiente AI.

Non esiste aggiornamento silenzioso o automatico dei progetti. La verifica delle nuove versioni e la loro installazione devono essere separate.

## 7. Validazione del repository sorgente

```bash
python tools/validate_repository.py
```

Lo script controlla la struttura dei file e la validità sintattica dei TOML. Non esegue test scientifici né verifica il comportamento degli agenti.
