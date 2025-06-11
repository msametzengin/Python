for i in range(3):
    password = input("Please enter ur password: ")
    if not password:
        print("This field cannot be left blank.")
    elif len(password) in range(3,9):
        print("New password is",password)
        break
    elif i==2:
        print("U have entered the wrong password three times. Please wait 15 minutes.")
    else:
        print("Your password is longer than 8 characters or shorter than 3 characters.")