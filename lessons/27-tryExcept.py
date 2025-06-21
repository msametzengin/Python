
try:
    numb1 = int(input("Number1 : "))
    numb2 = int(input("Number2 : "))
    final = numb1 / numb2

    print(final)

#except ZeroDivisionError:
#    print("A number cannot be divided by zero.")
    

#except ValueError:
#    print("Please enter numerical data.")


except (ZeroDivisionError,ValueError):
    print("There is a mistake")
