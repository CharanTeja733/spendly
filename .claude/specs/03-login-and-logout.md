# Spec: Login and Logout

## Overview

Implement the POST handler for `/login` so registered users can sign in with their email and password, and make `/logout` properly clear the session. The login form already exists in `login.html` and submits via POST to `/login`, but `app.py` only handles GET. This step wires up server-side authentication — credential validation, password verification, Flask session management, and conditional navigation — turning the app into a multi-page experience that knows who is signed in.

## Depends on

- **02-registration** — users must be able to create accounts (with hashed passwords) before they can sign in.

## Routes

- `POST /login` — authenticate user, create session, redirect to landing — public
- `GET /logout` — clear session, redirect to landing — public (always accessible; no-ops if not logged in)

## Database changes

No database changes. The `users` table (id, name, email, password_hash, created_at) already has everything needed for authentication.

## Templates

- **Modify:** `templates/base.html` — update the nav bar to show the user's name and a "Sign out" link when logged in, and "Sign in" / "Get started" links when logged out. Use `session.get("user_name")` to branch.
- **Modify:** `templates/login.html` — may need to preserve the email value on failed login attempt (stretch); the existing `{% if error %}` block is already sufficient.

## Files to change

- `app.py` — add `session` and `check_password_hash` imports; add POST handler for `/login`; replace the placeholder `/logout` with real session-clearing logic
- `templates/base.html` — conditional nav rendering based on login state

## Files to create

None.

## New dependencies

No new dependencies. Everything needed is already available:
- `werkzeug.security.check_password_hash` (partner to `generate_password_hash` already used in `database/db.py`)
- `flask.session` (built into Flask)
- `sqlite3` (standard library)

## Rules for implementation

- No SQLAlchemy or ORMs
- Parameterised queries only — never string-format SQL
- Passwords verified with `werkzeug.security.check_password_hash`
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Use Flask's `session` for login state (store `user_id` and `user_name`)
- On failed login, re-render the form with an error message ("Invalid email or password")
- On success, redirect to `/` (landing page) — the nav will update to show logged-in state
- `/logout` clears the session and redirects to `/` with a flash message
- The login error message should be generic ("Invalid email or password") — never reveal whether the email exists

## Definition of done

- [ ] Visiting `/login` (GET) shows the login form with email and password fields
- [ ] Submitting with a valid registered email and correct password signs the user in
- [ ] After sign-in, the nav bar shows the user's name and a "Sign out" link instead of "Sign in" / "Get started"
- [ ] Submitting with a wrong password shows "Invalid email or password" and does not sign in
- [ ] Submitting with an unregistered email shows "Invalid email or password" and does not sign in
- [ ] Clicking "Sign out" clears the session and redirects to `/` with a flash message
- [ ] After sign-out, the nav bar returns to showing "Sign in" / "Get started"
- [ ] All queries use parameterised SQL
