import sqlite3

class Client:
    def __init__(self, name, lastname, login, password):
        self.login = login
        self.password = password
        self.name = name
        self.lastname = lastname

    def __str__(self):
        print(self.name, self.lastname, self.login)

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('clients_data.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL,
                lastname TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def load_client(self):
        self.cursor.execute('''SELECT * FROM clients''')
        print(self.cursor.fetchall())

    def log_into(self, login, password):
        self.cursor.execute(
            "SELECT * FROM clients WHERE login = ? AND password = ?",
            (login, password,)
        )
        result = self.cursor.fetchone()
        if result:
            print("Login succeed")
            return True
        else:
            print("Login failed")
            return False
    
    def add_client(self, login, password, name, lastname):
        try:
            self.cursor.execute(
                "INSERT INTO clients (login, password, name, lastname) VALUES (?, ?, ?, ?)",
                (login, password, name, lastname)
            )
            self.connection.commit()
            print("New user created")
        except sqlite3.IntegrityError:
            print("User with this login already exists!")
        except Exception as e:
            print("Fail:", e)
    
    def delete_client(self, login):
        self.cursor.execute("DELETE FROM clients WHERE login = ?", (login,))
        self.connection.commit()
        print(f"Deleted client with login: {login}")

# #stworzyć kolejną klasę database i tam funkcje związane z requestami do bazy danych, logowania itd
# #używać fetchone

if __name__ == "__main__":
#     connection = sqlite3.connect('clients_data.db')
#     cursor = connection.cursor()

#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS clients (
#     login TEXT PRIMARY KEY,
#     password TEXT,
#     name TEXT,
#     lastname TEXT)''')

#     #test stuff
#     c1 = Client('John', 'Nowak', 'root', '1234')
#     # c1.add_client()
#     # try: print(c1)
#     # except: TypeError

#     c1.load_client()
#     c1.delete_client("root")

#     c1.load_client()
    db = Database()
    db.add_client("jank", "jan123", "jan", "kowalski")

#     connection.commit()
    db.close()