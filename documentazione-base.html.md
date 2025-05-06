# base.html

## Descrizione
Template base da cui estendono tutti gli altri. Include header, contenuto e footer comuni a tutte le pagine.

## Componenti principali
- `LINK` al file CSS statico `style.css`.
- `HEADER`: Include il blocco `header` personalizzabile dalle pagine figlie.
- `DIV`: Contenitore del blocco `content`.
- `FOOTER`: Footer statico con 3 paragrafi segnaposto.

## Note
Tutte le altre pagine `extend` questo template per riutilizzare layout e stile.
