# Spec: Registration

## Overview

Implement the POST handler for `/register` so visitors can create a Spendly account. The registration form already exists in `register.html` and submits to `/register` via POST, but `app.py` only handles GET. This step wires up the server-side logic — validation, duplicate-email check, password hashing, database insert, and redirect — making user registration a fully functional feature.

## Depends on

- **01-database-setup** — the `users` table and `get_db()` / `init_db()` must be working.

## Routes

- `POST /register` — process registration form, create user — public

## Database changes

No new tables or columns. The `users` table (id, name, email, password_hash, created_at) already covers everything needed.

## Templates

- **Modify:** `templates/register.html` — the form already exists; may need minor tweaks for flash-message support or keeping form values on error (stretch). The existing `{% if error %}` block is sufficient for server-rendered errors.
- **Modify:** `templates/base.html` — add a flash-message block above `{% block content %}` so success/error messages can render on any page.

## Files to change

- `app.py` — add POST handler for `/register`, add imports (`request`, `redirect`, `url_for`, `flash`)
- `templates/base.html` — add flash-message display
- `templates/register.html` — minor adjustments if needed (e.g. repopulate form fields on validation error)

## Files to create

None.

## New dependencies

No new dependencies. Everything needed is already available:
- `werkzeug.security.generate_password_hash` (already used in `database/db.py`)
- `sqlite3` (standard library)
- Flask's `request`, `redirect`, `url_for`, `flash` (Flask is already installed)

## Rules for implementation

- No SQLAlchemy or ORMs
- Parameterised queries only — never string-format SQL
- Passwords hashed with `werkzeug.security.generate_password_hash`
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Use Flask's `flash()` for success/error messages so they survive the redirect
- Validate server-side: name required, email required + valid-ish format, password min 8 chars
- On duplicate email, re-render the form with an error message
- On success, redirect to `/login` with a flash message

## Definition of done

- [ ] Visiting `/register` (GET) shows the registration form
- [ ] Submitting with valid name, email, and password creates a user in the database
- [ ] Password is stored hashed, never in plaintext
- [ ] Duplicate email shows an error and does not create a second user
- [ ] Empty fields or short password show validation errors
- [ ] On successful registration, user is redirected to `/login` with a success flash message
- [ ] Flash messages render on the page (verifiable by checking `/login` after registering)
- [ ] All queries use parameterised SQL
