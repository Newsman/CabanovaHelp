# Centrul de ajutor Cabanova

Sursa pentru [help.cabanova.com](https://help.cabanova.com). Fiecare modificare pe `main` se publică automat în ~1 minut (GitHub Actions → GitHub Pages).

## Cum modifici un articol

1. Deschide fișierul în `content/ro/<categorie>/<articol>.md` pe GitHub.
2. Apasă ✏️ (Edit), modifică textul, apoi **Commit changes**.
3. Gata: după ~1 minut modificarea e online (vezi tab-ul **Actions**).

## Articol nou

Creează `content/ro/<categorie>/<nume-scurt>.md`:

```markdown
---
title: "Titlul articolului"
description: "O frază care apare sub titlu și în Google."
weight: 3          # ordinea în categorie
---
Textul articolului.

## Subtitlu

- listă
1. pași numerotați

**text îngroșat**, [link spre alt articol](alt-articol), ![descriere imagine](img/nume.png)

> Sfat: apare într-un chenar evidențiat.
```

Imaginile se pun în `static/img/`. Categoriile sunt folderele din `content/ro/` (titlul, descrierea și iconița în `_index.md`).

## Reguli

- Editorul se numește **editorul PRO** / **Cabanova**. Nu menționa furnizorul editorului (verificarea automată oprește publicarea).
- `content/ro/editorul-vechi/` are articolele pentru editorul clasic (în engleză), importate de pe vechiul help.
- Textele de interfață (butoane, mesaje) sunt în `i18n/ro.toml`.

## Local (opțional)

`hugo server` (Hugo extended ≥ 0.169) — căutarea merge doar după `hugo && npx pagefind --site public`.
