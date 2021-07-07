import time
start_time = time.time()

def func_one(n):
    return list(map(str, range(n)))

chck1 = func_one(1000)
print(chck1)

end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)