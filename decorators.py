def func():
    return "Hello!!"

f = func()
print(f)

def new_decorator(oringinal_func):
    def wrap_func():
        print('Some extra code, before the original function')
        oringinal_func()
        print('Some extra code after the original function ')
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated")

dec = new_decorator(func_needs_decorator)

dec()
