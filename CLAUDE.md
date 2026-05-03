# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Status

This is a new Python project in early setup. No source code has been committed yet. Update this file as the stack is established.

## Design Documents

`design_docs/` contains planning materials for the Archimedes Metals website and e-commerce build (untracked). Consult these for product/content context.

## Stack

- **Framework:** Django 6
- **Package manager:** uv
- **Database:** SQLite (local), PostgreSQL (production)
- **Python:** 3.12

## Commands

```bash
uv run python manage.py runserver   # start dev server at localhost:8000
uv run python manage.py migrate     # apply database migrations
uv run python manage.py makemigrations  # generate migrations after model changes
uv run python manage.py createsuperuser # create admin user
uv run python manage.py test        # run tests
```

## Architecture

- `archimedes/` — Django project config (settings, root URLs, wsgi/asgi)
- `manage.py` — Django management entry point
- New features go in Django apps: `uv run python manage.py startapp <name>`
- Database: SQLite (`db.sqlite3`) for local dev
- Dependencies managed with uv (`pyproject.toml` + `uv.lock`)
