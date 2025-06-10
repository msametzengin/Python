"""
EXAMPLE:

customerAge = int(input("Please entering ur age: "))
ageofAdmission = 18
if customerAge < ageofAdmission:
    print("Unfortunately, you are not of the right age: ",customerAge)

else:
    print("Welcome ur age: ",customerAge)
"""

amountofMilk = int(input("Please entering amount of milk: "))
cheeseLimit = 11

if amountofMilk<cheeseLimit:
    print("Your milk quantity is not suitable for cheese: ",amountofMilk)
    print("The amount of milk you need to produce cheese is",(cheeseLimit-amountofMilk))

else:
    totalCheeseProduced = amountofMilk/cheeseLimit
    print("Total cheese produced is",int(totalCheeseProduced))



