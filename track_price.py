import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Boya-Microphone-Universal-Directional-Smartphone/dp/B076BCM26H/ref=sr_1_2?dchild=1&keywords=boya+mic&qid=1591025438&s=musical-instruments&sr=1-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}



def check_price():


    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    


    if(price < "1,700.00"):
        send_mail()

    print(price)
    print(title.strip())

    if(price < "1,700.00"):
        send_mail()


def send_mail():
    server = smtplib.smtp('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your email address','your password')

    subject = "Suprise, Price fell down!"
    body = "Check out the link https://www.amazon.in/Boya-Microphone-Universal-Directional-Smartphone/dp/B076BCM26H/ref=sr_1_2?dchild=1&keywords=boya+mic&qid=1591025438&s=musical-instruments&sr=1-2"


    msg = f"Subject: {subject}\n\n{body}"


    server.send_mail() (
        'enter from email address',
        'enter to email address',
        msg
    )

    print('Email has been sent')

    server.quit()


while(True):
    check_price()
    time.sleep(60*60)


