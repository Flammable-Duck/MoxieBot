import sqlite3
from datetime import datetime

def get_loan_info(uid):
    "Returns the loan info on a player via their user id"
    conn = sqlite3.connect("data/users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE uid= :uid", {'uid': uid})
    return c.fetchone()

def add_loan(uid, amt):
    "Adds a loan to the database"
    time = datetime.now().strftime("%d%m%Y%H%M%S")
    conn = sqlite3.connect("data/users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (':uid, :amt, :time')", {{'uid', uid}, {'amt', amt}, {'time', time}})
    conn.commit()
    conn.close()

def give_player_loan(uid, amt):
    add_loan(uid, amt)
