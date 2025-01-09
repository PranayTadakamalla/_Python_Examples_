# 1. Program to print numbers from 1 to n and calculate the sum using for and while loops
n = int(input("Enter a number: "))
a = 0
for i in range(1, n + 1):
    print(i)
    a += i
print("Sum using for loop: ",a)
b = 0
i = 1
while i <= n:
    print(i)
    b += i
    i += 1
print("Sum using while loop: ",b)


# 2. Program with a user-defined function calculate_square
def cal_sq(n):
    return n **2
n = int(input("Enter a positive integer: "))
a = cal_sq(n)
print("The square of", n, "is:", a)
