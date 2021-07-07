import requests
import bs4

res = requests.get("http://example.com")
print(res.text)

soup = bs4.BeautifulSoup(res.text, "lxml")
print(soup)
title = soup.select('title')
print(title)