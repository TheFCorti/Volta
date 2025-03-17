# Use case (ipotetico) del quiz

**Quiz**

**Livello dell'obiettivo: Funzionamento del quiz**

**Caso principale in caso di successo**
1) L'utente naviga verso la "piattaforma" clicca sull'icona del quiz
2) (Da rivedere) Si apre un modal / nuova pagina con l'inizio del quiz
3) Utente risponde alle domande
4) Il quiz termina

**Casi particolari**
- 1)
  - 1a) L'utente non è registrato allora si invita quest'utltimo a partecipare al quiz
  - 1b) L'utente è registrato (e loggato) allora si mostra il punteggio attuale
- 2)
  - 2a) L'utente inizia un nuovo quiz
  - 2b) L'utente ha un quiz non completato quindi si chiede di riprenderlo
- 3)
  - 3a) L'utente sceglie la risposta corretta, allora gli si dice che se vuole approfondire può trovare le informazioni ad uno specifico URL
  - 3b) L'utente sceglie la risposta errata, allora gli si dice l'URL della pagina dove può trovare le informazioni corrette
- 4)
  - 4a) In caso di "vincita" di un quiz si mostra una schermata di successo
  - 4b) In caso di "perdita" di un quiz si mostra una schermata di "retry"