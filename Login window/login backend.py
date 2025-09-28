import sqlite3

class Client():
    def __init__(self, name, lastname, login, password):
        self.login = login
        self.password = password
        self.name = name
        self.lastname = lastname
        self.connection = sqlite3.connect('clients_data.db')
        self.cursor = self.connection.cursor()

    # def __str__(self):
    #     print(self.name, self.lastname, self.login)

    def load_client(self):
        self.cursor.execute('''SELECT * FROM clients''')
        print(self.cursor.fetchall())
    
    def add_client(self):
        self.cursor.execute('''
        INSERT INTO clients (login, password, name, lastname)
        VALUES ('{}', '{}', '{}', '{}')
        '''.format(self.login, self.password, self.name, self.lastname))
        self.connection.commit()

connection = sqlite3.connect('clients_data.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
login TEXT PRIMARY KEY,
password TEXT,
name TEXT,
lastname TEXT)''')

#test stuff
c1 = Client('John', 'Nowak', 'root', '1234')
# c1.add_client()
# try: print(c1)
# except: TypeError

c1.load_client()

connection.commit()
connection.close()