from bs4 import BeautifulSoup
import requests, smtplib,os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('MY_PASSWORD')

recipient_email = os.getenv('RECIPIENT_EMAIL')

AMAZON_URL = "https://appbrewery.github.io/instant_pot/"

header = {
"Accept-Language": "en-US,en;q=0.6",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
}

response = requests.get(AMAZON_URL, headers=header)
response.raise_for_status()
amazon_url = response.text

soup = BeautifulSoup(amazon_url, "html.parser")
price = soup.find("span", class_="aok-offscreen").get_text()
price_split = price.split("$")
price = float (price_split[1])

if price < 100:

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(
        user=my_email,
        password=my_password
        )
        connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,
        msg=(f"Subject:Amazon Price Alert!!! \n\nInstant Pot Duo Plus 9-in-1 Electric Pressure Cooker,\
        Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker,\
         Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart  for just ${price}").encode("utf-8")
        )