import sqlite3


def top_users():
    "returns top 5 users, ordered by wealth"
    conn = sqlite3.connect('data/users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    users.sort(key=lambda a: a[1], reverse=True)
    return users[:5]

def search_user(uid):
    "returns a user"
    conn = sqlite3.connect('data/users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE uid= :uid", {'uid': uid})
    return c.fetchone()

def add_user(uid):
    "adds a new user to the database"
    conn = sqlite3.connect('data/users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (:uid, 100, 0)", {'uid': uid})
    conn.commit()
    conn.close()

def user_bal(uid):
    "returns a users balance"
    if str(search_user(uid)) == "None":
        add_user(uid)
        print("adding new user")
    return search_user(uid)[1]

def change_bal(uid, number):
    "add amount to user account"
    conn = sqlite3.connect('data/users.db')
    c = conn.cursor()
    new_bal = user_bal(uid) + number
    c.execute("UPDATE users SET bal = :bal WHERE uid = :uid", {'uid': uid, 'bal': new_bal})
    conn.commit()
    conn.close()
