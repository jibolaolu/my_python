def my_sum(*args):
    for items in args:
        print(items)
    return sum(args)

asum = my_sum(1,3,6,9,12,56)
print(asum)

#kwargs This comes in form of a dictionary

def myfunt(**kwargs):
    print(kwargs)
    if 'fruits' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruits']))
    else:
        print('My type of fruit cannot be found!!')

frut = myfunt(fruits='Apple', veggie = 'lettuce')
#print(frut)

def funct_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like to have {} {}'.format(args[0], kwargs['food']))

funct_args_kwargs(12,45,12,fruit = 'orange', food = 'amala', animal = 'parrot')

def myfunc(*args):
    for ar in args:
        if ar %2 == 0:
            print (ar)
    return ar

myfunc(12, 5,7,6,9)