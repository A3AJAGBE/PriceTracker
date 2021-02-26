import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.com/HP-14-inch-Chromebook-Touchscreen-Bluetooth/dp/B07L52KX7B/ref=sr_1_21?dchild=1" \
              "&keywords=student+laptop&qid=1614330419&s=pc&sr=1-21 "
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/14.0.3 Safari/605.1.15",
    "Accept-Language": "en-us"
}

# Get the project page from Amazon
response = requests.get(PRODUCT_URL, headers=HEADERS)
response.raise_for_status()
data = response.text

# Scrape the web for the price
soup = BeautifulSoup(data, "lxml")
product_price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
price = product_price.getText()
print(price)
