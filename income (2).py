import sqlite3
import datetime
#date in form of YYYY/MM/DD HH:MM:SS (24hr)
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = sqlite3.connect("nea.db")
#create income table
def income_db():
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS income(id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, amount REAL NOT NULL, category TEXT NOT NULL, description TEXT, date TEXT NOT NULL, FOREIGN KEY (user_id) REFERENCES login(id)
        )
    """)
    conn.commit()

#add the income into table
def add_income(username, amount, category, description, date):
    c = conn.cursor()
    c.execute("SELECT id FROM login WHERE username = ?", (username,))
    row = c.fetchone()
    if not row:
        return False
    else:
        user_id = row[0]
        c.execute("""
            INSERT INTO income(user_id, amount, category, description, date)
            VALUES (?, ?, ?, ?, ?)
            """, (user_id, amount, category, description, date))
        conn.commit()

    return True

#get all data from expenses table
def get_income(username):
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
            ORDER BY date desc
            """, (user_id,))
        return c.fetchall()

def delete_income(income_id):
    c=conn.cursor()
    c.execute("DELETE FROM income WHERE id = ?", (income_id,))
    conn.commit()

