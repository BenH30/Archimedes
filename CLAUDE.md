# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Archimedes Metals — custom architectural metal fabrication company in Dallas–Fort Worth. The website is a lead-capture and credibility platform targeting general contractors, architects, interior designers, commercial property owners, sign companies, and millwork firms. Positioning: specialty architectural metal partner, not a generic fabrication shop.

## Design Documents

`design_docs/` contains planning materials (untracked). Key files:
- `Archimedes_Website Content DRAFT v4_with e-commerce.docx` — page-by-page content drafts, brand messaging, tagline ("Fabricating a World Worth Looking At"), and SEO guidance
- `Archimedes_Metals_Marketing_Assessment_Chat_April_2026.pdf` — target customer segments, keyword strategy, website recommendations
- `Archimedes_Metals_Fabrication_Catalog.pdf` — 36-page project showcase; source of truth for the `/projects/` page and the crimson color scheme (`#b0063a`)

## Stack

- **Framework:** Django 6 + Python 3.12
- **Package manager:** uv
- **CSS:** Tailwind CSS v4 (standalone CLI at `~/.local/bin/tailwindcss`)
- **Fonts:** Barlow Condensed (display/headlines) + Barlow (body) via Google Fonts
- **Database:** SQLite (local), PostgreSQL (production)

## Commands

```bash
uv run python manage.py runserver        # dev server at localhost:8000
uv run python manage.py migrate          # apply database migrations
uv run python manage.py makemigrations   # generate migrations after model changes
uv run python manage.py createsuperuser  # create admin user
uv run python manage.py test             # run tests
tailwindcss -i static/css/input.css -o static/css/output.css --minify  # recompile CSS
```

Always recompile CSS after editing `static/css/input.css` or adding new Tailwind classes that weren't previously used.

## Architecture

- `archimedes/` — Django project config (settings, root URLs, wsgi/asgi)
- `core/` — main Django app; all current views, URLs, and static content data
- `templates/` — global templates directory (base.html + all page templates)
- `static/css/input.css` — Tailwind source; `output.css` is the compiled artifact
- New Django apps: `uv run python manage.py startapp <name>`

### Template & CSS Patterns

All pages extend `templates/base.html`. Page sections follow this pattern:
- Dark hero: `bg-[#08111f]` with diagonal stripe texture (inline style), left crimson accent line, location tag with crimson `w-8 h-px` rule, `font-display font-black uppercase` headline
- Section labels: `flex items-center gap-4` with `w-8 h-px bg-[#b0063a]` + small-caps text
- Brand colors: `#08111f` (dark navy), `#b0063a` (crimson), `#cc0a45` (crimson hover), `#0f172a` (navy)
- No rounded corners on buttons — use sharp edges throughout
- CTAs: `bg-[#b0063a]` primary, `bg-[#08111f]` secondary, `bg-white text-[#b0063a]` on crimson backgrounds

## Page Inventory

| Page | URL | Status |
|------|-----|--------|
| Homepage | `/` | ✅ Complete |
| About | `/about/` | ✅ Complete |
| Quote / Contact | `/quote/` | ✅ Complete (form renders; email sending not yet wired) |
| Privacy Policy | `/privacy/` | ✅ Complete |
| Architectural Metalwork | `/services/architectural-metalwork/` | ⬜ Not built |
| Metal Wall Panels | `/services/metal-wall-panels/` | ⬜ Not built |
| Custom Metal Signage | `/services/custom-metal-signage/` | ⬜ Not built |
| Fencing, Screens & Enclosures | `/services/fencing-screens-enclosures/` | ⬜ Not built |
| Shelving, Trim & Brass Features | `/services/shelving-trim-brass/` | ⬜ Not built |
| Press Brake & Forming | `/services/press-brake-forming/` | ⬜ Not built |
| Welding | `/services/welding/` | ⬜ Not built |
| Coatings & Finishes | `/services/coatings-finishes/` | ⬜ Not built |
| Projects / Gallery | `/projects/` | ✅ Complete (21 projects, 7 categories from fabrication catalog) |
| Shop Built Products | `/shop/` | ⬜ Not built |
