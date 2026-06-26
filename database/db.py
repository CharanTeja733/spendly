import sqlite3
import os

from werkzeug.security import generate_password_hash

# ------------------------------------------------------------------ #
# Configuration                                                       #
# ------------------------------------------------------------------ #

# DB file lives at project root (same level as app.py)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(PROJECT_ROOT, "spendly.db")


# ------------------------------------------------------------------ #
# Connection                                                          #
# ------------------------------------------------------------------ #

def get_db():
    """Return a SQLite connection with row_factory and foreign keys enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# ------------------------------------------------------------------ #
# Schema                                                              #
# ------------------------------------------------------------------ #

def init_db():
    """Create all tables if they don't already exist."""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            name            TEXT    NOT NULL,
            email           TEXT    NOT NULL UNIQUE,
            password_hash   TEXT    NOT NULL,
            created_at      TEXT    DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id         INTEGER NOT NULL,
            amount          REAL    NOT NULL,
            category        TEXT    NOT NULL,
            date            TEXT    NOT NULL,
            description     TEXT,
            created_at      TEXT    DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


# ------------------------------------------------------------------ #
# Seed data                                                           #
# ------------------------------------------------------------------ #

# Fixed category list per the spec
CATEGORIES = ["Food", "Transport", "Bills", "Health", "Entertainment", "Shopping", "Other"]


def seed_db():
    """Insert demo data if the users table is empty."""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return  # already seeded

    # Demo user
    cursor.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@spendly.com", generate_password_hash("demo123")),
    )
    user_id = cursor.lastrowid

    # 8 sample expenses spread across all 7 categories, dates in June 2026
    sample_expenses = [
        (user_id, 250.00, "Food",         "2026-06-24",   "Zomato dinner order"),
        (user_id, 45.00,  "Transport",    "2026-06-25",   "Auto to office"),
        (user_id, 1200.00,"Bills",        "2026-06-01",   "Electricity bill"),
        (user_id, 350.00, "Health",       "2026-06-15",   "Pharmacy — vitamins"),
        (user_id, 500.00, "Entertainment","2026-06-18",   "Movie tickets + popcorn"),
        (user_id, 899.00, "Shopping",     "2026-06-20",   "T-shirt from Myntra"),
        (user_id, 160.00, "Other",        "2026-06-10",   "Stationery supplies"),
        (user_id, 680.00, "Food",         "2026-06-22",   "Grocery run — BigBasket"),
    ]

    cursor.executemany(
        "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
        sample_expenses,
    )

    conn.commit()
    conn.close()
