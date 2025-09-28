import sqlite3

class Client():
    def __init__(self, name, lastname, login, password):
        self.name = name
        self.lastname = lastname
        self.login = login
        self.password = password
        self.connection = sqlite3.connect('clients_data.db')
        self.cursor = self.connection.cursor()

    def __str__(self):
        print(self.name, self.lastname, self.login)

    def load_client(self):
        self.cursor.execute('''SELECT * FROM clients''')
        print(self.cursor.fetchall())
    
    def add_client(self):
        self.cursor.execute('''
        INSERT INTO clients (name, lastname, login, password)
        VALUES ('{}', '{}', '{}', '{}')
        '''.format(self.name, self.lastname, self.login, self.password))
        self.connection.commit()


connection = sqlite3.connect('clients_data.db')
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS clients (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT,
# lastname TEXT,
# login TEXT,
# password TEXT)''')

c1 = Client('John', 'Nowak', 'root', '1234')
c1.add_client()
print(c1)

connection.commit()
connection.close()