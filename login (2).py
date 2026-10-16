import sqlite3
from cryptography.fernet import Fernet

conn = sqlite3.connect("nea.db")

#create a login database
def login_db():
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS login(id INTEGER PRIMARY KEY, username TEXT NOT NULL, password_encrypted TEXT NOT NULL)""")
    conn.commit()
    return conn

#validate username and password to requirements
def validate_username(username):
    if len(username) <7 or len(username)>15:
        return False
    return True

def validate_password(password):
    special = "!@$%^&*()-_=+[]{}\\|;:\"',./<>?~"
    if len(password) <7:
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char in special for char in password):
        return False

    return True

#encrypt password
def create_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()
try:
    load_key()
except:
    create_key()
fernet = Fernet(load_key())

def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted):
    return fernet.decrypt(encrypted.encode()).decode()

#register the user
def registration(username, password):
    if not (validate_username(username) and validate_password(password)):
        return False

    c = conn.cursor()
    #check if username has already been registered
    c.execute("SELECT * from login WHERE username = ?", (username,))
    if c.fetchone():
        return False

    password_encrypted = encrypt_password(password)
    #insert the username and encrypted password into db
    c.execute("INSERT INTO login(username, password_encrypted) VALUES (?,?)", (username, password_encrypted))
    conn.commit()
    return True

#login the user
def login(username, password):
    c = conn.cursor()
    #check whether user exists in db
    c.execute("SELECT username from login WHERE username = ?", (username,))
    if not c.fetchone():
        return False
    else:
        #check if password matches username
        c.execute("SELECT password_encrypted From login WHERE username = ?", (username,))
        row = c.fetchone()
        if not row:
            return False
        #check if the password inputted matches the decrypted password
        stored_password = decrypt_password(row[0])
        if stored_password != password:
                return False
    return True