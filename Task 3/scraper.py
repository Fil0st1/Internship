import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.bbc.com/news')

soup = BeautifulSoup(r.text, "html.parser")

tags = soup.find_all('h2')

headlines = []
for t in tags:
    text = t.get_text(strip=True)
    if text:             
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for h in headlines:
        file.write(h + "\n")
