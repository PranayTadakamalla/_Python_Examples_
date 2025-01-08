n = int(input("Enter a positive integer: "))
a = 0
for i in range(2, n+1, 2):
    a += i
print("Sum of even numbers:", a)
