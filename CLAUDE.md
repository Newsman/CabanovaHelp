# CabanovaHelp: reguli de lucru

Centrul de ajutor Cabanova (help.cabanova.com): Hugo + Pagefind, publicat automat pe GitHub Pages la push pe `main` (`.github/workflows/pages.yml`). Repo **public**. Răspunde în română, scurt; utilizatorul vrea lucru rapid și eficient, cu propuneri proactive.

- Editorul e white label: doar „editorul PRO” și „Cabanova”; numele furnizorului nu apare nicăieri (nici în cod sau comentarii); CI-ul oprește publicarea dacă apare.
- Limbi: RO prioritar, apoi en, de, fr, pt (`[languages]` în `hugo.toml`, `content/<limbă>`, `i18n/<limbă>.toml`). Articolele PRO sunt principale; `editorul-vechi/` (legacy, EN) separat, la căutare apare după PRO.
- Conținut: editorul PRO (din FAQ-ul furnizorului, rescris, fără numele lui); domenii, cont, plăți din cabanova.com și vechiul help; email: doar strictul necesar din kb.newsman.ro. Nu inventa setări tehnice (servere, DNS): cere-le utilizatorului.
- Design: aceleași culori/fonturi ca site-ul nou (Figtree, Plus Jakarta Sans, #4376AB, hero #F2F6FB), header/footer minimale. Linkurile spre site-ul principal folosesc `params.main` (la lansarea cabanova.com nou: `https://www.cabanova.com`).
- Căutarea: Pagefind (`assets/help.js`); conținutul indexat e doar `<article data-pagefind-body>`. URL-urile vechi `/<slug>.html` sunt redirecționate din `layouts/404.html`.
- Toate URL-urile prin `relURL`/`RelPermalink` (site-ul poate rula într-un subfolder pe GitHub Pages).
- Test local: `hugo --minify -b http://localhost:8099/ -d /tmp/hp && npx pagefind --site /tmp/hp`, apoi Playwright (Chrome desktop + mobil). Capturi doar când contează aspectul.
- Commit-uri cu autorul utilizatorului (Florian Cosmin Mircea).
