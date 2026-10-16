import sqlite3
import datetime
#date in form of YYYY/MM/DD HH:MM:SS (24hr)
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = sqlite3.connect("nea.db")

#craete the expenses table
def expense_db():
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expense(id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, amount REAL NOT NULL, category TEXT NOT NULL, description TEXT, date TEXT NOT NULL, FOREIGN KEY(user_id) REFERENCES login(id)
        )
        """)
    conn.commit()

#add expenses to the table crreated
def add_expense(username, amount, category, description, date):
    c = conn.cursor()
    c.execute("SELECT id from login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
        #insert values into table
        c.execute("""
            INSERT INTO expense(user_id, amount, category, description, date)
            VALUES (?, ?, ?, ?, ?)
            """, (user_id, amount, category, description, date))
        conn.commit()

    return True

#retrieve the expenses
def get_expense(username):
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
            ORDER BY date desc
            """, (user_id,))
        return c.fetchall()

def delete_expense(expense_id):
    c = conn.cursor()
    c.execute("DELETE FROM expense where id = ?", (expense_id,))
    conn.commit()
