import string
#Function that returns the volume of a sphere
import alphabet as alphabet


def vol(rad):
    return (4/3)*(3.14)*(rad **3)

vl = vol(2)
print(vl)

#Write a function that checks whether a number is given range(inclusive of high and low)
def run_check(num, low, high):
    if num in range(low,high+1):
        print(f'{num} is definitely in range')
    else:
        print(f'{num} is out of range')

run_check(11,5,10)

#Write a function that calculates the number of uppercase and lowercase letter in a string

def alpha_check(str):
    lower_case = 0
    upper_case = 0
    for st in str:
        if st.isupper():
            upper_case += 1
        elif st.islower():
            lower_case += 1
        else:
            pass
    print(f'The original string is {wrd}')
    print(f'lower case count is {lower_case}')
    print(f'Upper case count is {upper_case}')

wrd = 'The world we living Today is SomeTHING else'
alpha_check(wrd)

#Or
def alpha_check2(str):
    d = {'lower': 0, 'upper': 0}

    for st in str:
        if st.isupper():
            d['upper'] += 1
        elif st.islower():
            d['lower'] += 1
        else:
            pass
    print(f'The original string is {wrd}')
    print(f'lower case count is {d["lower"]}')
    print(f'Upper case count is {d["upper"]}')

secapl= alpha_check2(wrd)

#Write a function that returns a unique in a list
def uniq(lst):
    x = []
    for uni in lst:
        if uni not in x:
            x.append(uni)
    return x

list = [1,1,1,1,2,2,2,5,57,7,7,8]

uni = uniq(list)
print(uni)

#Python function to multiply al the numbers in the list
def mul_lst(lst):
    final_ans = 1
    for i in lst:
        final_ans = final_ans * i
    return final_ans

fin_ans = mul_lst(list)
print(fin_ans)


#Write a python that checks a word is palindrome or not
def palindrome(strng):
    strng = strng.replace(' ', '')
    return strng == strng[::-1]

pali = palindrome('madam')
print(pali)

#Write a function that check a string is a pangram or not
def pangram(pan, alphabet=string.ascii_lowercase):
    alpha = set(alphabet)
    pan = pan.replace(' ','')
    pan = pan.lower()
    pan= set(pan)
    return pan == alpha

strr = pangram('The quick brown fox jumps over the lazy dog')
print(strr)
