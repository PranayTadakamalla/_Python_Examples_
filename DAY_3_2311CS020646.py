a = float(input("Enter marks for subject 1: "))
b = float(input("Enter marks for subject 2: "))
c = float(input("Enter marks for subject 3: "))
average = (a + b + c) / 3
if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")
