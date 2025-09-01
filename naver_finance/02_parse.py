import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/item/main.naver?code=010140"
res = requests.get(url)
bsobj = BeautifulSoup(res.text, "html.parser")

div_today = bsobj.find("div", {"class":"today"})
em = div_today.find("em")
price = em.find("span")
print(price)