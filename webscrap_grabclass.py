import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
#print(soup)
toc = soup.select('.toctext')[0]
print(list(toc))

first_item = soup.select('.toctext')[0]
print(first_item)
txt = first_item.text
print(txt)

for item in soup.select('.toctext'):
    print(item.text)
