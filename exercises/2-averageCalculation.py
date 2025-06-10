
midtermPoint = int(input("Please entering midterm exam note: "))
finalPoint = int(input("Please entering final exam note: "))

averagePoint = midtermPoint*0.4 + finalPoint*0.6

if finalPoint<30:
    print("Ur final point is under than 30. Thats why FF")
elif averagePoint>=90:
    print("Congrats AA:",averagePoint)
elif 85<=averagePoint<90:
    print("Well done BA:",averagePoint)
elif 80<=averagePoint<85:
    print("Well done BB:",averagePoint)
elif 70<=averagePoint<80:
    print("Good CB:",averagePoint)
elif 60<=averagePoint<70:
    print("Good CC:",averagePoint)
elif 50<=averagePoint<60:
    print("You passed the lesson DD",averagePoint)
else:
    print("Please work harder :( FF",averagePoint)