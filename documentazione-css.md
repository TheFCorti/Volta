# Documentazione del foglio di stile (`style.css`)

## Selettori globali

### `*`
Applica uno stile di reset globale a tutti gli elementi della pagina (rimuove margini e padding, imposta il box-sizing).

### `body`
Definisce lo stile generale del corpo della pagina: font, colori, sfondo, altezza minima e layout flessibile verticale.

---

## Intestazione

### `header`
Definisce lo stile della sezione di intestazione, con sfondo blu, padding e disposizione centrata degli elementi.

### `header form`
Stilizza i form contenuti all'interno dell'header, con spaziatura (`gap`) tra i bottoni e supporto al layout responsive (wrap).

---

## Bottoni

### `input[type="submit"]`
Stilizza i bottoni di invio: colore blu, testo bianco, padding e bordi arrotondati. Include animazione al passaggio del mouse.

### `input[type="submit"]:hover`
Modifica lo stile del bottone quando il cursore passa sopra: colore più scuro e leggera animazione di sollevamento.

---

## Home (pagina index)

### `.volta-image`
Definisce uno sfondo con immagine e overlay scuro per effetto contrastato, impostando altezza e posizionamento.

### `.volta-text`
Testo centrato sull’immagine grazie a `position: absolute` e `transform`.

---

## Contenuto principale

### `div.content`
Contenitore principale del contenuto: padding, sfondo bianco, bordi arrotondati e ombra.

---

## Testo

### `p`
Stilizza i paragrafi con margine inferiore e dimensione del font maggiore.

---

## Form e input avanzati

### `form[action*="details"]`
Stile specifico per i form che inviano verso URL contenenti "details". Allineamento centrale e spaziatura.

### `select`
Menu a tendina con padding, bordi personalizzati e larghezza predefinita.

---

## Sezioni non ancora usate

### `block.details`
Definito per sezioni di dettaglio ma attualmente non utilizzato nelle pagine HTML.

### `.highlight`
Classe utility per evidenziare testo con colore e grassetto. Non ancora implementata.

---

## Footer

### `footer`
Stilizza il piè di pagina con sfondo blu, testo bianco e padding.

### `footer p`
Paragrafi all’interno del footer: testo centrato e dimensione ridotta.

---

## Responsive Design

### `@media (max-width: 768px)`
Regole per schermi piccoli:
- Padding e margini ridotti
- Form in colonna
- Elementi `select` e bottoni più ampi

---

## Classi utilitarie

### `.center-text`
Centra orizzontalmente il testo.

---

## Gamification – Quiz

### `#risposte_date`
Contenitore delle risposte già date: sfondo blu chiaro, layout flessibile e bordi arrotondati.

### `#D1, #D2, #D3, #D4`
Stile delle risposte passate: sfondo blu scuro, larghezza e altezza proporzionali.

### `#domanda`
Box per la domanda del quiz: sfondo blu, bordi evidenti, altezza e larghezza fisse.

### `#risposte_quiz`
Contenitore per le risposte correnti. Disposto in riga, con spaziatura tra le opzioni.

### `#A1, #A2, #A3, #A4`
Bottoni di risposta: sfondo blu chiaro, bordi evidenti, larghezza e altezza standardizzate.

---

## Nota finale

- Le sezioni `.highlight` e `block.details` non sono ancora in uso ma possono essere implementate.

