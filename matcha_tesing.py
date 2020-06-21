import sqlite3

conn = sqlite3.connect(':memory:')

dbase  = conn.cursor()
dbase.execute("""CREATE TABLE matcha (
                username text,
                email text, 
                password text
                )""")

conn.commit()

dbase.execute("INSERT INTO matcha values ('test', 'test@test', 'pass')")

conn.commit()

dbase.execute("SELECT * FROM matcha")

print(dbase.fetchall())

conn.close()


class Matcha:

    def __int__(self, username, email, password):
        self.username   = username
        self.email      = email
        self.password   = password

    def __repr__(self):
        return f"Matcha User('{self.username}', '{self.email}', '{self.password}')"