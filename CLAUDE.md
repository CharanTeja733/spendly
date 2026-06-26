# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Spendly — a personal expense tracker built with Flask. The app is under active construction; many routes are placeholders. It follows a step-by-step curriculum where features (database, auth, CRUD) are implemented incrementally.

## Commands

```bash
# Run the app (dev mode, auto-reload)
python app.py          # listens on http://localhost:5001

# Run tests
pytest
```

## Architecture

```
app.py                  # Flask app — all routes live here for now
database/
  db.py                 # SQLite layer (get_db / init_db / seed_db — to be implemented)
templates/
  base.html             # Base layout (nav, footer, CSS/JS includes) — extended by every page
  landing.html          # Landing page with hero, features, CTA, and video modal
  register.html         # Registration form (name, email, password)
  login.html            # Login form (email, password)
  terms.html / privacy.html  # Static legal pages
static/
  css/style.css         # All styles (single file, ~750 lines, custom properties on :root)
  js/main.js            # Shared JS (currently empty — students add interactivity here)
```

**Template inheritance**: `base.html` is the single layout. Every page extends it via `{% extends "base.html" %}` and fills `{% block title %}`, `{% block content %}`, and optionally `{% block head %}` / `{% block scripts %}`.

**CSS**: Design tokens live as custom properties on `:root` in `style.css` — colors (`--ink`, `--paper`, `--accent`, etc.), fonts (`--font-display: DM Serif Display`, `--font-body: DM Sans`), spacing, and radii. The palette is a warm off-white paper background with dark ink text and a dark green accent (`#1a472a`). All styles are vanilla CSS — no framework, no build step.

**Database** (`database/db.py`): Currently a placeholder. When implemented, it exports three functions:
- `get_db()` — returns a SQLite connection with `row_factory = sqlite3.Row` and foreign keys enabled
- `init_db()` — `CREATE TABLE IF NOT EXISTS` for all tables
- `seed_db()` — inserts demo data if tables are empty

**No JS framework**: All interactivity uses vanilla JavaScript. The video modal in `landing.html` sets this pattern — inline `<script>` block, no library imports.

## Route map

| Route | Method | Status | Template |
|---|---|---|---|
| `/` | GET | Done | `landing.html` |
| `/register` | GET | Form only (no POST) | `register.html` |
| `/login` | GET | Form only (no POST) | `login.html` |
| `/terms` | GET | Done | `terms.html` |
| `/privacy` | GET | Done | `privacy.html` |
| `/logout` | GET | Placeholder | — |
| `/profile` | GET | Placeholder | — |
| `/expenses/add` | GET | Placeholder | — |
| `/expenses/<id>/edit` | GET | Placeholder | — |
| `/expenses/<id>/delete` | GET | Placeholder | — |
