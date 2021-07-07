mylist = []
strng = 'Oluwaseun'

for ayo in strng:
    mylist.append(ayo)

name = print(mylist[4])

##ListComprehension

mlist = [tam for tam in strng]
print(mlist)

sea = [num ** 2 for num in range(0,11,2) if num %2 == 0]
print(sea)