import sqlite3

conn = sqlite3.connect("nea.db")

def categories_db():
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, name TEXT NOT NULL, FOREIGN KEY(user_id) REFERENCES login(id)
        )
        """)
    conn.commit()
categories_db()  

def add_category(username, name):
    c =conn.cursor()
    c.execute("SELECT id from login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
        c.execute("""
            INSERT INTO categories (user_id, name)
            VALUES (?, ?)
        """, (user_id, name))
        conn.commit()

def get_category(username):
    c = conn.cursor()
    c.execute("SELECT id FROM login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
    c.execute("""
        SELECT id, name
        FROM categories
        WHERE user_id = ?
        """, (user_id,))
    return c.fetchall()

def delete_category(category_id):
    c=conn.cursor()
    c.execute("DELETE FROM categories WHERE id = ?", (category_id,))
    conn.commit()
