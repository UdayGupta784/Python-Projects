import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")


soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all("div",class_="quote")

for quote in quotes:
    text =quote.find("span",class_="text")
    author=quote.find("small",class_="author")
    print(text.get_text())
    print(author.get_text())
    print("----------------------------")