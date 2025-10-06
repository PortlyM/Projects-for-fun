import login_backend

db = login_backend.Database()

while True:
    choice = int(input("what do you want to do? \n1. log in\n2. sign in \n"))
    if choice == 1:
        login = input("Write login: ")
        password = input("write password: ")
        res = db.log_into(login, password)
        if res != False:
            print(res)
            client = login_backend.Client(res[3], res[4], res[1], res[2])
            break

    elif choice == 2:
        name = input("write name: ")
        last_name = input("write lastname: ")
        login = input("write login: ")
        password = input("Write password: ")
        client = login_backend.Client(name, last_name, login, password)
        #print(client)
        db.add_client(login, password, name, last_name)

    else:
        print("Write appropriate number!")

print(f"Siema {client.name}")