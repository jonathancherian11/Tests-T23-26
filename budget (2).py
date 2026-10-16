import sqlite3

conn = sqlite3.connect("nea.db")

def budget_db():
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS budget(user_id INTEGER PRIMARY KEY, amount REAL NOT NULL, spent REAL NOT NULL DEFAULT 0, FOREIGN KEY (user_id) REFERENCES login(id))
        """)
    conn.commit()

def set_budget(username, amount):
    c =conn.cursor()
    c.execute("SELECT id from login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
        c.execute("""
            INSERT INTO budget(user_id, amount, spent)
            VALUES (?, ?, 0)
            ON CONFLICT(user_id) DO UPDATE SET amount = excluded.amount
        """, (user_id, amount))
        conn.commit()

def get_budget(username):
    c = conn.cursor()
    c.execute("SELECT id FROM login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
        c.execute("SELECT amount, spent FROM budget WHERE user_id =?", (user_id,))
        row = c.fetchone()
        if not row:
            return (0, 0)
        else:
            return row

def update_spent(username, amount):
    c=conn.cursor()
    c.execute("SELECT id FROM login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
        c.execute("""
            INSERT INTO budget (user_id, amount, spent)
            VALUES (?, 0, ?)
            ON CONFLICT(user_id) DO UPDATE SET spent = spent + excluded.spent
        """, (amount, user_id))
        conn.commit()   
