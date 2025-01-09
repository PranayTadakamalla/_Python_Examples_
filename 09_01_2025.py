
'''list = [1,2,3,4,5,6]
iterate_var = iter(list)
print(iterate_var)
for i in iterate_var:
    if i%2==0:
        print(i)
'''
list1 = list(range(1,21))
#print(list1)
iterate_var = iter(list1[0:6])
for i in iterate_var:
    if i>5:
        print(i)