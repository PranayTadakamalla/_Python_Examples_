import pandas as pd
Study_Hours = [10,8,2,4]
Student_Name = ["Abc","Def","Ghi","Jkl"]
Unique_Id = [1,3,5,8]
dict1 = {"Unique_Id":Unique_Id,"Student_Name":Student_Name,"Study_Hours":Study_Hours}
print(dict1)
df = pd.DataFrame(dict1)
print(df)