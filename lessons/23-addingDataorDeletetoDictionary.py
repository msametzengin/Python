
superLeague = {"Galatasaray":"63","Fenerbahce":"62","Besiktas":"61"}

for i,j in superLeague.items():
    print(i,":",j)

superLeague.pop("Galatasaray") #deleting


while True:
    addingTeam = input("Enter team: ")
    addingPoint = input("Enter points: ")
    superLeague.setdefault(addingTeam,addingPoint) #adding

    for i,j in superLeague.items():
        print(i,":",j)

    choose = input("Do you want to exit the program? T/F: ")
    if choose == "T":
        break
    else:
        pass
