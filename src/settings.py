import sqlite3

conn = sqlite3.connect('settings.db')

c = conn.cursor()

# c.execute("""CREATE TABLE settings (
#             setting text,
#             value text
#             )""")
# c.execute(""" INSERT into settings VALUES ('prefix', '$')""")
# c.execute("INSERT INTO settings VALUES (:setting, :prefix)", {
#           'setting': "prefix", 'prefix': "$"})

c.execute("SELECT * FROM settings where prefix='$'")
print(c.fetchall())

conn.commit
conn.close()
