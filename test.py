flavour = ["strawberry", "banana", "vanilla"]

for flav in flavour:
    print(flav)

st = "Print only the words that start s in this sentence"
for s in st.split():
    if s[0].lower() == 's':
        print(s)

# Print all even number from 0 to 10
for x in range(0,11):
    if x %2==0:
        print(x)

## List comprehension for number between 1 and 50 but divisible by 3
numb = [ta for ta in range(1,51) if ta %3 == 0]
print(numb)


#Print EVEN when the length of a word is even
str = "Print every words in this sentence that has an even number of letters in this sentence"
for j in str.split():
    if len(j) %2 == 0:
        print(j + " It's EVEN !!")

## Print Fizz if its multiple of 3 and Buzz for multiple of 5, fizzbuzz for both in number between 1-100##

for y in range(1,101):
    if y%3 == 0 and y%5 == 0:
        print("FIZZ-BUZZ")
    elif y%3 == 0:
        print("FIZZ")
    elif y%5 == 0:
        print("BUZZ")
    else:
        print("{} is not divisible by 3 or 5".format(y))

## Use list-comprehension to create a list of the first letter of the sentence
nut = "Create a list of the first letters of every word in this sentence"
for i in nut.split():
     print (i[0])

buh = [j[0] for j in nut.split()]
print(buh)