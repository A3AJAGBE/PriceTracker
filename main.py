import os
import smtplib

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

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
product_price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
product_title = soup.find(id="productTitle").getText()
price = float(product_price.split('$')[1])
title = product_title.strip()

# The amount you want to pay for the product
TARGET_PRICE = 250

# Email config
EMAIL = os.environ.get('GMAIL')
PASSWORD = os.environ.get('GMAIL_PASS')
RECEIVER_EMAIL = os.environ.get('YMAIL')
SMTP = os.environ.get('SMTP_ADDRESS')

# Send an email if the product price is low or equal to the target price
if price <= TARGET_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP, port=587) as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PASSWORD)
        conn.sendmail(
            from_addr=EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:Chrome Laptop Price Alert\n\n{message}\n{PRODUCT_URL}"
        )

