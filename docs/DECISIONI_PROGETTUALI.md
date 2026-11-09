# Decisioni progettuali consolidate

Questo documento riassume le scelte emerse durante la raccolta dei requisiti.

1. Prodotto: libreria modulare e riutilizzabile di agenti e skill, non applicazione autonoma.
2. Piattaforme: massima portabilità, con adattatori quando necessari.
3. Agenti: nove ruoli effettivi; il frazionamento del comando è un protocollo generale.
4. Skill: universali, condivise e in forma esclusivamente testuale.
5. Agenti: ricevono il contesto; intervengono quando l'argomento è pertinente al proprio ruolo.
6. Analisi: indipendenti e parallele quando possibile; niente dibattito diretto obbligatorio tra agenti.
7. Memoria: `PROJECT_SYNTHESIS.md` in Markdown nella radice di ogni progetto.
8. Scrittura memoria: solo il Sintetizzatore può modificarla; aggiornamento a fine step.
9. Archivio analisi: conservare selettivamente contributi importanti, divergenze e criticità.
10. Obiettivi: definiti all'inizio con risultati attesi e criteri di completamento.
11. Fasi: il Coordinatore verifica e presenta un rapporto; l'utente approva il passaggio.
12. Obiettivi in evoluzione: il Coordinatore può proporre cambiamenti; l'utente li approva.
13. Fonti: riportare i link delle fonti effettivamente usate.
14. Interlocuzione: questionari brevi di 3–5 domande, chiuse e con spazio aperto facoltativo.
15. Disaccordi: sintesi trasparente delle posizioni; decide l'utente.
16. Correzioni: massimo tre tentativi dell'agente originario, con controllo del Coordinatore.
17. Autorizzazioni: attività preparatorie libere; modifiche sostanziali soggette ad approvazione per intervento.
18. Repository: unico repository centrale, installazione completa o selettiva.
19. Personalizzazione: niente varianti locali permanenti; le modifiche si gestiscono nel repository centrale.
20. Aggiornamenti: verifica e proposta; installazione dopo approvazione.
21. Lingua: italiano.
22. Backup/versionamento: nessun sistema imposto dal framework.

## Punto interpretato con cautela

L'utente ha indicato che, durante un intervento autorizzato, il sistema può applicare autonomamente modifiche impreviste se necessarie. Questa facoltà è interpretata in modo prudenziale: riguarda interventi accessori, reversibili e a basso rischio entro il perimetro autorizzato. Non si estende a obiettivi, requisiti, dati, metodologie, algoritmi, codice scientifico o architettura sostanziale, che richiedono nuova autorizzazione.
