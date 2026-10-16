import income
import expense
import sqlite3

conn = sqlite3.connect("nea.db")

def g_income(username):
    c = conn.cursor()
    c.execute("SELECT id FROM login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
        #select all items
        c.execute("""
            SELECT amount, category, description, date, id
            FROM income
            WHERE user_id = ?
            """, (user_id,))
        return c.fetchall()

def g_expense(username):
    c = conn.cursor()
    c.execute("SELECT id FROM login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
        #select all items
        c.execute("""
            SELECT amount, category, description, date, id
            FROM expense
            WHERE user_id = ?
            """, (user_id,))
        return c.fetchall()