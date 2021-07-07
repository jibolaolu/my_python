##MAP
def square(n):
    return n **2

num = [1,2,4,5,6]
for item in map(square, num):
    print(item)

se = list(map(square,num))
print(se)

def splicer(mystring):
    if len(mystring)%2  == 0:
        return 'EVEN'
    else:
        return mystring[0]

name = ['Adee', 'John', 'Sally']
sli = list(map(splicer, name))
print(sli)

#FILTER

def check_even(eve):
    return eve %2 ==0

myeve = [1,2,3,6,7,9,10]

evee = list(filter(check_even, myeve))
print(evee)

for i in filter(check_even,myeve):
    print(i)