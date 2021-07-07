def square():
    try:
        for i in ['a','b','c']:
            print(i ** 2)
    except:
        print("General error watch out")

#2

try:
    b = 5
    c = 0
    d = b/c
except:
    print("Error")
finally:
    print("All DONE!")


def int_square():
    while True:
        try:
            sq = int(input("Kindly enter a number !! "))
            sqr = sq ** 2
            print("The final ans shld be {}".format(sqr))
        except:
            print("An Error occured please try again !")
            continue
        else:
            break
        finally:
            print("The Code has finally ran")
    print("Your number square is: ")
    print(sqr)


df = int_square()