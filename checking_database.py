import sqlite3
conn = sqlite3.connect('bloodbank.db')
c = conn.cursor()

c.execute("DELETE FROM donar_table WHERE rowid= 8")
conn.commit()
conn.close()