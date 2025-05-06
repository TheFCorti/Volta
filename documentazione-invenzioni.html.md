# invenzioni.html

## Descrizione
Pagina che mostra una lista a tendina di invenzioni selezionabili. Può essere estesa per mostrare dettagli (come in `details.html`).

## Estende
`base.html`

## Blocchi definiti
- `header`: Navigazione completa.
- `content`: Form con select per scegliere un'invenzione, con invio POST e CSRF token.
- `details`: Blocco interno al content sovrascrivibile (vedi `details.html`).

## Variabili richieste
- `invenzioni`: lista di nomi di invenzioni da mostrare nella `select`.
