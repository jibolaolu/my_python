x = 0
while x < 5:
    print(f'This is the current value {x}')
    x += 1
else:
    print('X is not less than 5')

name = 'Seanny'

for letter in name:
    if letter == 'e':
        break
    print(letter)

for num in range(0,11,2):
    print(num)

index_count = 0
for letter in 'abcdef':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count +=1

##Enumerate
word = 'abcde'
for index, letta in enumerate(word):
    print(index)
    print(letta)
    print('\n')

###ZIP####

lst1 = [1, 2, 3]
lst2 = ['Jane', 'Jude', 'Tam']
zip(lst1, lst2)

for item in zip(lst1, lst2):
    print(item)
