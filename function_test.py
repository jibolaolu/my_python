#1 Write a function that returns lesser of two given numbers if both numbers are even,
# but returns the greater if one or both are odd

def lesser_of_two_evens(a,b):
    if a %2 == 0 and b %2 == 0:
        #BOTH NUMBERS ARE EVEN
       return min(a,b)
    else:
        #IF ONE OR BOTH NUMBERS ARE ODD
        return max(a,b)

ress = lesser_of_two_evens(3,5)
print(ress)

#ANIMAL_CHECKER
def animal_checker(text):
    word_list = text.lower().split()

    first_word = word_list[0]
    second_word = word_list[1]

    return first_word[0] == second_word[0]

cra = animal_checker('crazy cat')
print(cra)

def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

twen = makes_twenty(10,10)

#Converting letters to Upper or Lower

def old_letter(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return first_letter.upper() + inbetween + fourth_letter.upper()+ rest

mac = old_letter('macdonalds')
print(mac)


#reverse the words in a sentence
def rev_text(text):
    wordlist = text.split()
    reversed_word_list = wordlist[::-1]
    return ' '.join(reversed_word_list)

rt = rev_text('are we going home')
print(rt)

#Almost there; Given an integer n, return True of n is within10 of either 100 or 200

def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200 - n)<= 10)

almthr = almost_there(295)
print(almthr)


