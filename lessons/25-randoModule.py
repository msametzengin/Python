
import random

a = random.random() # Produces numbers between 0 and 1

b = random.uniform(1.5,2.5) # Produces numbers between 1.5 and 2.5

c = random.randint(20,100) # Produces numbers between 20 and 100 

dList = ["Samet","Zengin","23","Kutahya"]

d = random.choice(dList) # Randomly selects from the list.

# random.shuffle(dList) # Shuffles the elements in the list.

print(random.sample(dList,2)) # Allows us to sample from the list. 