from bs4 import BeautifulSoup
import requests, smtplib,os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('MY_PASSWORD')

recipient_email = os.getenv('RECIPIENT_EMAIL')

AMAZON_URL = "https://www.amazon.com/Samsung-Smartphone-Unlocked-Res-Camera-Warranty/dp/B0FG1THCD7/ref=sr_1_3?_encoding=UTF8&sr=8-3"

header = {
"Accept-Language": "en-US,en;q=0.6",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
}

response = requests.get(AMAZON_URL, headers=header)
response.raise_for_status()
amazon_url = response.text

soup = BeautifulSoup(amazon_url, "html.parser")
price = soup.find("span", class_="a-offscreen").get_text()
price_float = float(price.replace('$', ''))


if price < 400:

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(
        user=my_email,
        password=my_password
        )
        connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,
        msg=(f"Subject:Samsung Galaxy S25  Price Alert!!! \n\nSamsung Galaxy S25 FE Cell Phone (2025), 256GB AI Smartphone,\
        Unlocked Android, Large Display, 4900mAh Battery, High Res-Camera, AI Photo Edits, Durable, US 1 Yr Warranty, JetBlack.\
        for just ${price}").encode("utf-8")
        )


