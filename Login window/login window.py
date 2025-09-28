import sqlite3

connection = sqlite3.connect('clients_data.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
lastname TEXT,
login TEXT,
password TEXT''')

cursor.execute('''
INSERT INTO clients (name, lastname, login, password)
VALUES ('Anna', 'Nowak', 'annanowak123', 'annanowak123')
''')

cursor.execute('''
SELECT * FROM clients''')

print(cursor.fetchall())

connection.commit()
connection.close()