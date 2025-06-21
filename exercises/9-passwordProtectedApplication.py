import subprocess as sp

psw = "123456"
userPW = input("Please enter the password: ")
if userPW == psw:
    while True:
        Choice = input("1-Notepad\n2-Calculator\n3-Chrome\nq-Exit\n")

        if Choice == "1":
            sp.call("notepad.exe")
        elif Choice == "2":
            sp.call("calc.exe")
        elif Choice == "3":
            sp.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
        elif Choice == "q":
            break
        else:
            print("Try again...\n")
else:
    print("Go")
