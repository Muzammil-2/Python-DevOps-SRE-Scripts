predefine_username = "Muzammil"
predefine_password = "Muza123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == predefine_username:
    if password == predefine_password:
        print ("successfully login! welcome!")
    else:
        print("incorrect password")
else:
    print("incorrect username")