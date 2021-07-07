import requests
import bs4

res = requests.get("http://quotes.toscrape.com")
soup = bs4.BeautifulSoup(res.text, 'lxml')
#print(soup.select('.author'))

authors = set()

for name in soup.select('.author'):
    authors.add(name.text)
print(authors)

print(soup.select('.text'))

quotes = []

for quote in soup.select('.text'):
    quotes.append(quote.text)
print(quotes)

for item in soup.select('.tag-item'):
    print(item.text)
