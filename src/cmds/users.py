import sqlite3
# conn = sqlite3.connect('data/users.db')
# c = conn.cursor()

# c.execute("""CREATE TABLE users(
#     uid text,
#     bal interger
# )""")


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
    c.execute("INSERT INTO users VALUES (:uid, 100)", {'uid': uid})
    conn.commit()
    conn.close()
    
def user_bal(uid):
    "returns a users balance"
    if str(search_user(uid)) == "None":
        add_user(uid)
        print("adding new user")
    _, bal = search_user(uid)
    return bal

def change_bal(uid, number):
    "add amount to user account"
    conn = sqlite3.connect('data/users.db')
    c = conn.cursor()
    new_bal = user_bal(uid) + number
    c.execute("UPDATE users SET bal = :bal WHERE uid = :uid", {'uid': uid, 'bal': new_bal})
    conn.commit()
    conn.close()

# print(search_user("434826300105031683"))
# print(user_bal("434826300105031683"))
#change_bal("434826300105031683", 100)
#print(user_bal("434826300105031683"))
# print(user_bal("testDelMe"))
# insert_employee(emp_1)
# c.execute("SELECT * FROM employees WHERE uid='doe'")
# conn.commit()
# conn.close()
