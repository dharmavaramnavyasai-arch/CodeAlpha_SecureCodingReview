import getpass

attempts = 3

while attempts > 0:
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username == "admin" and password == "admin123":
        print("Login Successful")
        break

    attempts -= 1
    print("Wrong Password")

if attempts == 0:
    print("Account Locked")