
dbUsername = "admin"
dbPw = 1234

while True: # infinity loop
    username = input("Please entering ur username: ")
    password = int(input("Please entering ur password: "))

    if dbUsername == username and dbPw == password:
        print("Welcome: ",username)
        break
    elif dbUsername == username and dbPw != password:
        print("Ur password is wrong please try again.")
        answer = input("Do you want to change your password? t/f:")
        if answer=="t":
            print("Ur password is changing...")
            newPassword = int(input("Please entering ur new password: "))
            dbPw = newPassword
            print("Ur password is changed.")
    elif dbUsername != username and dbPw == password:
        print("Ur username is wrong please try again.")
    else:
        print("Ur username and password are wrong. please try again.")
        
