from collections import Counter
from collections import defaultdict
from collections import namedtuple

mylist = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
lst = Counter(mylist)
print(lst)

d = {'a': 10}

d = defaultdict(lambda: 0)

d ['correct'] = 100

print(d['correct'])

print(d['wrong key'])

Dog = namedtuple()

