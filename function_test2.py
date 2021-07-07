def has_33(nums):
    for i in range(0, len(nums) -1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    else:
        return False

chck = has_33([3,3,3])
print(chck)

#PaperDoll; given a character.. return 3 same characters in a word
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result

paper = paper_doll('seaun')
print(paper)

#BlackJack
def black_jack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) > 21:
        return sum([a,b,c])-10
    else:
        return 'BURST!!'

blckjack = black_jack(10,16,15)
print(blckjack)

#Summer 69 return the sum in an array skipping numbers that starts with 6 and extending to 9

def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

summer = summer_69([1,3,5,6,8,9,10])
print(summer)

#Spy-Game
def spy_game(lst):
    code = [0,0,7, 'x']
    for ls in lst:
        if ls == code[0]:
            code.pop(0)
    return len(code) == 1

game = spy_game([1,7,2,9,0,8,7])
print(game)

#Count prime; write a function that returns the number of a prime number that exist up to and including
# a given number
def count_primes(num):

    #check for 0 or 1 input
    if num < 2:
        return 0
    primes = [2]
    x = 3
    while x <= num:
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

chckprimes = count_primes(100)




