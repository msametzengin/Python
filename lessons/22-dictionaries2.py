
superLeague = {"Galatasaray":"63","Fenerbahce":"62","Besiktas":"61"}

team = input("Please write the team you want to learn the standings of(Galatasaray,Fenerbahce,Besiktas): ").capitalize()

"""
if team not in superLeague:
    print("The team you selected is not on the list.")
else:
    print(team,":",superLeague[team])
"""

print(team,":",superLeague.get(team,"The team u selected is not on the list."))
