
def calculateWater(kilogram):
    manCalculate = kilogram*0.04
    womanCalculate = kilogram*0.03

    gender = input("Please writing ur gender? (woman/man): ").lower()

    if gender == "woman":
        print("*"*30)
        print("Your gender: ",gender)
        print(womanCalculate,"liters u should drink!")
        print("*"*30)
    elif gender == "man":
        print("*"*30)
        print("Your gender: ",gender)
        print(manCalculate,"liters u should drink!")
        print("*"*30)
    elif not gender:

        print("Please specify your gender")
    else:

        print("U wrote something wrong or incomplete.")

weight=int(input("Please entering ur weight(kgs): "))
calculateWater(weight)