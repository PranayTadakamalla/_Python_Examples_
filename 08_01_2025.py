'''
import pandas as pd
Study_Hours = [10,8,2,4]
Student_Name = ["Abc","Def","Ghi","Jkl"]
Unique_Id = [1,3,5,8]
dict1 = {"Unique_Id":Unique_Id,"Student_Name":Student_Name,"Study_Hours":Study_Hours}
print(dict1)
df = pd.DataFrame(dict1)
print(df)
'''
'''
#List Comprehension
list = [1,2,3,4,5]
res = [i for i in list if i%2!=0]
print(res)
res = [i for i in list if i%2==0]
print(res)
res = [i for i in list]
print(res)
'''
''''
#Dictionary Comprehension
dict = {"a":12,"abc:":123,"def":45}
result = {value:key for key,value in dict.items()}
print(result)
result = {key:value for key,value in dict.items()}
print(result)
'''
'''
#Tuple Comprehension
import math as m
numbers = [1,2,3,4]
result = tuple(i**1/2 for i in numbers)
result = tuple(m.sqrt(i) for i in numbers)
print(result)
'''
'''
#E-Commerce Example
a = [{"name": "Laptop", "price": 800},{"name": "Smartphone", "price": 500},{"name": "Tablet", "price": 300}]
b = {i["name"]: i["price"] for i in a if i["price"] <= 500}
print(b)
'''
'''
a = [1,2,3,4,5]
b = [i**2 for i in a]
print(b)
c = [i**2 for i in range(1,6)]
print(c)
print([i**2 for i in range(1,6)])
'''
'''
a = ["mam","bro","wow"]
b = [i for i in a if i == i[::-1]]
print(b)
print([i for i in a if i == i[::-1]])
'''
'''
a = [1,2,3,4,5]
b = [6,7,5,2,8,9,1]
print([i for i in a if i in b])
'''