
uppercaseLetters = "NE MUTLU TÜRK'ÜM DİYENE".lower() # makes all letters lowercase.
lowercaseLetters = "ne mutlu türküm diyene".upper() # makes all letters uppercase.
capitalizeLetter = "ne mutlu".capitalize() # capitalizes only the first letter.
reverseLetters = "Ne muTlu".swapcase()
'''
If the letters are lowercase, it makes them uppercase, 
if they are uppercase, it makes them lowercase.
'''

# print() u can also use these func in print()

delete = "++++Samet++".strip("+") # deletes all +'s.

# print("Samet","Zengin",sep="+",end=":") => Samet+Zengin:
name = "Samet"
surName = "Zengin"
age = 23
print("Person's name: {}\nPerson's surname: {}\nPerson's age: {}".format(name,surName,age))
# format is useful or f parameter
print(f"Person's name: {name}\nPerson's surname: {surName}\nPerson's age: {age}")



