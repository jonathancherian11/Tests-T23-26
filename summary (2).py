import sqlite3
conn = sqlite3.connect("nea.db")

def income_total(username, start_date):
    c=conn.cursor()
    c.execute("SELECT id from login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
        c.execute("""
            SELECT SUM(amount)
            FROM income
            WHERE user_id = ?
            AND datetime(date) >= datetime(?)
        """, (user_id, start_date))
        row = c.fetchone()[0]
        if not row:
            return 0
        else:
            return row

def expense_total(username, start_date):
    c=conn.cursor()
    c.execute("SELECT id from login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
        c.execute("""
            SELECT SUM(amount)
            FROM expense
            WHERE user_id = ?
            AND datetime(date) >= datetime(?)
        """, (user_id, start_date))
        row = c.fetchone()[0]
        if not row:
            return 0
        else:
            return row