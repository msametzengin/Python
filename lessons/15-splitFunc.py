"""
test = "samet,zengin,fenerbahce"
test = test.split(",")
print(test)

date = "17/04/2002"
date = date.split("/")
print(date)
"""

getData = input("Please write the words to be broken down: ")

for i in getData.split():
    print(i[0], end="")



