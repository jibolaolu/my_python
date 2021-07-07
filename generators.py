import random
def create_square(n):
    for i in range(n):
      yield i**3

for x in create_square(10):
    print(x)
#sq = create_square(5)
#print(sq)

def generate_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in generate_fibon(9):
    print(num)


random.randint(1,10)

def rand_num(low, high,n):
    for j in range(n):
        yield random.randint(low ,high)

for se in rand_num(1,12,15):
    print(se)

