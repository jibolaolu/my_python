name = 'This is a global variable'

def greet():
    name= 'Tammy'

    def hello():
        print('Hello ' + name)

    hello()

grt = greet()
#print(grt)