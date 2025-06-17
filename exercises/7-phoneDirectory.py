phoneDirectory = dict()

def addPhoneNo(x):

    print("***Welcome to add phone number***")
    getName = input("Please write name: ")
    getNumber = input("Please write number: ")

    x = phoneDirectory.setdefault(getName,getNumber)
    print(f"Added a person named {getName}")

def showPhoneDirectory(x):

    numberofPeople = len(x)
    print("***Welcome to phone directory***")
    print(f"The number of people is => {numberofPeople}")
    for i,j in x.items():
        print(i,":",j)

def deletingName(x):

    deletingPerson = input("Enter the person to be deleted:")
    x = phoneDirectory.pop(deletingPerson)
    print()

while True:
    
    print("***WELCOME***")
    print("Choose one(1,2,3,4)")
    makeaChoice = int(input("1-Add\n2-Delete\n3-See Phone Directory\n4-Quit\n"))

    if makeaChoice == 4:
        break
    elif makeaChoice == 1:
        addPhoneNo(phoneDirectory)
    elif makeaChoice == 2:
        deletingName(phoneDirectory)
    elif makeaChoice == 3:
        showPhoneDirectory(phoneDirectory)
    else:
        print("Please write one of 1-2-3-4.")



