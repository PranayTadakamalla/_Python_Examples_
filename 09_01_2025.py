'''list = [1,2,3,4,5,6]
iterate_var = iter(list)
print(iterate_var)
for i in iterate_var:
    if i%2==0:
        print(i)
'''
'''
list1 = list(range(1,21))
print(list1)
iterate_var = [1,2,3,4,5,6]
iterate_var = iter(list1[0:6])
for i in iterate_var:
    if i>5:
        print(i+1)
'''
'''
def s(n):
    for i in range(n):
        yield i + 2

for i in s(10):
    print(i)
'''
'''
def s(n):
    for i in range(n):
        if i>5:
            yield i**2
for i in s(10):
    print(i)
'''
'''
a = lambda x,y,z: x*y*z
print(a(2,3,5))
'''
'''
def sample(func):
    def wrapper(item):
        item = item.upper()
        return func(item)
    return wrapper
@sample
def process(item):
    return item
result = process
print(result("hello world!"))
'''
'''
def sample(func):
    def wrapper(item):
        item = item.lower()
        return func(item)
    return wrapper
@sample
def process(item):
    return item
result = process
print(result("HELLO WORLD!"))
'''
'''
def add(func):
    def wrapper(a, b):
        return func(a, b)
    return wrapper
@add
def ab(a, b):
    return a + b
result = ab
print(result(5, 10))
'''
'''
def a(func):
    def b():
        for i in range(1, 11):
            func(i)
    return b
@a
def c(n):
    print(n)
c()
'''
'''
import pandas as pd
Study_Hours = [10,8,2,4]
Student_Name = ["Abc","Def","Ghi","Jkl"]
Unique_Id = [1,3,5,8]
dict1 = {"Unique_Id":Unique_Id,"Student_Name":Student_Name,"Study_Hours":Study_Hours}
df = pd.DataFrame(dict1)
print(df)
print(df.head(1))
print(df.iloc[::,:1])
print(df.tail(1))
print(df.iloc[::,:-1])
'''