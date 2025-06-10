
feverDegree = float(input("Please entering ur fever degree: "))
cough = input("Do you have a cough? T/F :").lower()
headAche = input("Do you have a headache? T/F :").lower()
day = int(input("How long have you had complaints? :"))

if feverDegree>=39:
    if day>=3:
        print("WARNING!! go to hospital. ")
    else:
        print("Ur fever is borderline. If it continues, go to the hospital. ")
if (feverDegree>=39) and (cough=="t") and (headAche=="t") and (day>=3):
    print("Please go to the nearest healthcare facility.")

# Depending on the situation, you can continue like this. if else if elif etc...