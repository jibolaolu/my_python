import re

text = "The agent's phone number is 07932441600 phone"
pattern = 'NONe on'
res = re.search(pattern, text)
print(res)
mtc = re.findall('phone', text)
print(len(mtc))

for match in re.finditer('phone', text):
    print(match.span())

phnenub = "My phone number is 079-8556-1556"
phe = re.search(r'\d{3}-\d{4}-\d{4}', phnenub)
print(phe)


##Additional regex
chck = re.search(r'cat|dog', 'The cat is looking through the window')
print(chck)

al = re.findall(r'...at', 'There are five cats wearing hats that sat over there')
print(al)

phrase = "There are 3 numbers inside 34 5 this sentence"
patter = r'[^\d]+'
phr = re.findall(patter, phrase)
print(phr)

test_sentn = "This is  string!! But it has punctuation marks. How can we remove it ?"
tst = re.findall(r'[^!.?]+',test_sentn)
print(tst)

join_back = ' '.join(tst)
print(join_back)

textt = "Only find the hyphen-words in this sentence. But you do not know how long-ish"

pat = r'[\w]+-[\w]+'
txt = re.findall(pat, textt)
print(txt)

#Grouping multiple options
sentn1 = "Hello, would you like some catfish?"
sentn2 = "Hello would you like some catnap?"
sentn3 = "Hello, have you seen this caterpillar?"

sen_re = re.search(r'cat(fish|nap|erpillar)', sentn3)
print(sen_re)
