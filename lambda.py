def square(num):
    return num ** 2

squr = lambda numb: numb **2
sq = squr(5)
print(sq)

#Lambda with map function
mynum = [1,2,4,3,5]
sec = list(map(lambda num: num**2,mynum ))
print(sec)


#Lambda with filter
fil = list(filter(lambda num: num%2 == 0, mynum))
print(fil)
