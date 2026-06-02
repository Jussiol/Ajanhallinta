# Ajanhallinta

Python-komentorivityökalu arjen tärkeiden osa-alueiden kierrättämiseen.

Ohjelma arpoo seuraavan aktiviteetin FIFO-pohjaisella estologiikalla, jotta samat kategoriat eivät toistu liian usein.Projektikategoria kierrättää projekteja hitaammalla syklillä.

Aktiviteetit ja projektit (harrastukset tms) voi konfiguroida asetukset.jsonissa "kaikki" kohtiin.

Valinnat estetään hetkellisesti FIFO-logiikalla, jotta samat asiat eivät toistu liian usein.

## Käyttö

```bash
python main.py