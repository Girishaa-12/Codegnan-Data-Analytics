'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

url = "https://www.crossword.in/?srsltid=AfmBOorxUI5V2Z9p3cTj5I9OPNy-mrsevEHATz0f1Tvy2LmSfUAKFXxl"

try:
    response = requests.get(url)
    response.encoding = "utf-8"
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

soup = BeautifulSoup(response.text, features="html.parser")

books = soup.find_all(name="article", class_="product_pod")

names = []
prices = []

for book in books:
    name = book.h3.a["title"]
    price_text = book.find("p", class_="price_color").text

    names.append(name)
    prices.append(price_text)

df = pd.DataFrame({
    "Book_Name": names,
    "Price": prices
})

print(df)
print(df.shape)
print(df.head())

df.to_csv("books_data.csv", index=False)

print("CSV File Saved Successfully!")

plt.figure(figsize=(10,5))

plt.bar(
    df["Book_Name"][:10],
    df["Price"][:10]
)

plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price (£)")
plt.title("Top 10 Book Prices")
plt.tight_layout()
plt.show()
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

url = "https://books.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

names = []
prices = []

for book in books:
    name = book.h3.a["title"]
    price_text = book.find("p", class_="price_color").text
    price = float(re.sub(r"[^\d.]", "", price_text))

    names.append(name)
    prices.append(price)

df = pd.DataFrame({
    "Book_Name": names,
    "Price": prices
})

print(df.head())

plt.figure(figsize=(10, 5))
plt.bar(df["Book_Name"][:10], df["Price"][:10])

plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Top 10 Book Prices")

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
