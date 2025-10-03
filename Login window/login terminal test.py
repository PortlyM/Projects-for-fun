import login_backend

db = login_backend.Database

while True:
    choice = int(input("what do you want to do? \n1. log in\n2. sign in \n"))
    if choice == 1:
        login = input("Write login: ")
        password = input("write password: ")
        db.log_into(login, password)
        

    elif choice == 2:
        name = input("write name: ")
        last_name = input("write lastname: ")
        login = input("write login: ")
        password = input("Write password: ")
        client = login_backend.Client(name, last_name, login, password)
        #print(client)
        db.add_client(1, login, password, name, last_name)

    else:
        print("Write appropriate number!")