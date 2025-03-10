# Documetazione HTML

## Struttura logica dei file

- Homepage
- Biografia
- Invenzioni
  - Pila
  - Metano
- Tempio Voltiano
- Informazioni sul progetto

## Struttura di ogni pagina

```html
<html>
    <head>
        <title>Titolo pagina</title>
        <!-- Fogli di stile -->
    </head>
    <body>
        <center>
            <!-- Navbar: sezioni sito -->
            <header>
            </header>
            <br>
            <div>
                <!-- Contenuto pagina -->
            </div>
            <footer>
                <!-- Collegamenti -->
            <footer>
        </center>
    </body>
</html>
```

### Elementi principali di ogni pagina:
1. Header
2. Div (contenuto della pagina)
3. Footer

#### 1 Header
Contiene dei pulsanti i quali effettuano una chiamata GET al server, con un URL specifico, il quale restituisce una pagina HTML con le relative risorse (CSS, immagini, video...); tutte le pagine hanno una struttura ben delineata che comprende i [componenti citati sopra](#struttura-di-ogni-pagina).
Il render della pagina avviene lato server.
#### 2 Div (contenuto della pagina)
Nel contenuto della pagina è presente il contenuto informativo principale come: testo, immagini, video, audio.
#### Footer
Il footer contiene i collegamenti alla pagine del sito e informazioni di contatto.
### Pagine
- #### Homepage
  Presentazione progetto
- #### Biografia
  - Vita, (invenzioni e opere) di Alessandro Volta
- #### Invenzioni
  La pagina delle invenzioni contiene un menu per selezionare l'invenzione desiderata, le informazioni riguardanti l'invenzione vengono mostrare al di sotto del menu per selezionare l'invenzione
- #### Tempio Voltiano
  Informazioni Tempio Voltiano
- #### Informazioni sul progetto
  - Autori del progetto
  - Gruppi coinvolti
