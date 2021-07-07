import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')
img = soup.select('.thumbimage')[0]
print(img['src'])

gt_img = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png")
print(gt_img.content)

f= open('my_image.png', 'wb')
f.write(gt_img.content)
f.close()