# Architettura del framework

## 1. Obiettivo

Fornire una libreria riutilizzabile di agenti e skill universali per accompagnare progetti scientifici, tecnici, professionali e software dall'idea iniziale alla manutenzione. Il framework non è legato a una singola piattaforma e non costituisce un'applicazione autonoma.

## 2. Livelli

1. **Regole centrali:** comportamento comune, processo decisionale, autorizzazioni e memoria.
2. **Agenti:** ruoli con responsabilità distinte.
3. **Skill:** procedure testuali condivise, richiamate quando pertinenti.
4. **Adattatori:** rappresentazioni specifiche richieste dalle piattaforme.
5. **Memoria del progetto:** `PROJECT_SYNTHESIS.md`, collocato nella radice del progetto operativo.

## 3. Principio di separazione

La definizione canonica di ciascun agente è conservata in `agents/`. La configurazione Antigravity è in `.agents/agents/`; la configurazione Codex è in `.codex/agents/`. Le skill canoniche e operative si trovano in `.agents/skills/` perché il percorso è condiviso da più ambienti compatibili.

Le copie degli adattatori devono essere aggiornate insieme alla definizione canonica. Non modificarle separatamente: le modifiche devono partire dal contenuto canonico e poi essere propagate agli adattatori.

## 4. Agenti

- **Coordinatore:** direzione del lavoro, selezione degli agenti, comunicazione, controllo qualità e gestione delle autorizzazioni.
- **Interlocutore:** dialogo, chiarezza delle intenzioni, domande e conferme.
- **Curioso:** emersione di requisiti e opportunità non espresse.
- **Critico:** ricerca di limiti, rischi e debolezze.
- **Professore:** verifica scientifica e metodologica.
- **Consigliere:** ricerca di alternative.
- **Bilancia:** compromessi tra rigore e praticità.
- **Spia:** ricerca comparativa di prodotti, metodi e precedenti.
- **Sintetizzatore:** sintesi e manutenzione della memoria condivisa.

## 5. Regole di collaborazione

Tutti gli agenti devono conoscere la sintesi corrente prima di iniziare un nuovo incarico. All'avvio di un nuovo progetto, nella raccolta iniziale dei requisiti e nella prima pianificazione, il Coordinatore consulta tutti gli agenti disponibili con incarichi distinti e coerenti con i rispettivi ruoli; anche chi non rileva contributi pertinenti lo dichiara brevemente.

Le valutazioni indipendenti vengono avviate in parallelo quando la piattaforma lo consente e non vi sono dipendenze; altrimenti si procede in sequenza mantenendo indipendenti i giudizi e dichiarando il limite. Negli step successivi il Coordinatore seleziona gli agenti pertinenti e motiva le esclusioni non ovvie nel piano o nel rapporto. La consultazione completa si ripete per un nuovo progetto o un cambiamento sostanziale di obiettivi o perimetro. Il Sintetizzatore organizza i contributi dopo il controllo qualità del Coordinatore. Non è previsto un dibattito diretto obbligatorio tra agenti.

Il Coordinatore controlla ogni contributo prima del suo utilizzo. Il Sintetizzatore raccoglie i contributi controllati, espone divergenze e aggiorna la memoria alla fine di ogni step completato.

## 6. Competenze

Le skill sono universali e condivise. Non sono associate in modo esclusivo a un singolo agente. Ogni agente può usare le skill pertinenti. Le skill forniscono procedure, non concedono permessi operativi.

## 7. Limiti

La capacità di avviare subagenti, eseguire lavori in parallelo, accedere al terminale o usare strumenti esterni dipende dalla piattaforma e dai permessi disponibili. Un file di configurazione non può conferire capacità che l'ambiente non possiede.
