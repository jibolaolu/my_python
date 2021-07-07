def even_check(num):
    if num % 2 == 0:
        return "its Even"

sean = even_check(34)
print(sean)

#Return true of any numbers is even inside a list

def even_check_list(num_list):
    even_number = []
    for num in num_list:
        if num % 2 == 0:
            even_number.append(num)
        else:
            pass
    return even_number

ay = even_check_list([1, 4, 5])
print(ay)