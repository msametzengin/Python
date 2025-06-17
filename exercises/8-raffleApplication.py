import random

users = list()

def addUsers(x):
    print("-"*30)
    addUser = input("The user you want to add:")
    x.append(addUser)
def showUsers(x):
    count = 1
    print("-"*30)
    for i in x:
        print(str(count)+"-User: ",i)
        count+=1
    print("-"*30)
def randomPersonPick(x):
    count = 1
    print("-"*30)
    selectPerson = int(input("How many people should be chosen ?:"))
    chooseRandomly = random.sample(x,selectPerson)
    for i in chooseRandomly:
        print(str(count)+"-User: ",i)
        count+=1
    print("-"*30)
def swapUsers(x):
    count = 1
    print("-"*30)
    random.shuffle(x)
    for i in x:
        print(str(count)+"-User: ",i)
        count+=1
    print("-"*30)

while True:
    print("****Welcome****")
    choice = int(input("1-Add User\n2-See Users\n3-Choose Randomly\n4-Shuffle Users\n5-Exit\n"))

    if choice == 1:
        addUsers(users)
    elif choice == 2:
        showUsers(users)
    elif choice == 3:
        swapUsers(users)
    elif choice == 4:
        randomPersonPick(users)
    elif choice == 5:
        break
    else:
        print("Wrong, try again!")