import sqlite3
#connecting to the database
conn = sqlite3.connect('bloodbank.db')

#creating cursor over the connection to execute commands
c = conn.cursor()

# creating a table
c.execute("""CREATE TABLE donar_table(
			name text,
			blood_type text,
			donate_organs text,
			phone_number text,
			email text,
			address text
)""")

#commiting to the database
conn.commit()

#closing the connection
conn.close()