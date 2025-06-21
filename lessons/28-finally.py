import time

try:
    numb1 = int(input("Number1 : "))
    numb2 = int(input("Number2 : "))
    final = numb1 / numb2

    print(final)

except ValueError:
    print("Please enter numerical data.")

finally:
    counter = 5
    
    for i in range(5):
        time.sleep(1)
        print("Countdown:",counter)
        counter-=1
        if counter == 0:
            print("Transaction completed...")

