tests = [1,5,'Sean', 'Tom']

for sean in tests:
    print(sean)

num = [12, 11, 14,60,77]

num_sum = 0

for lsum in num:
    num_sum = num_sum + lsum
print(num_sum)

##### For-loop tuple

tup = (1,2,5)
for j in tup:
    print(j)

mylist = [(1,2), (3,5), (7,8)]
for lst in mylist:
    print(lst)

#Tuple-Unpacking
for (a,b) in mylist:
    print(a)
    print(b)

##For-loop Dictionar##

dct = {'Name': 'Tome', 'State':'Chicago', 'Occupation': 'Engineer'}

for dc in dct.items():
     print(dc)

for k,v in dct.items():
    print(v)