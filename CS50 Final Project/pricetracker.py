import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://scalperscompany.com/collections/hombre-nueva-coleccion-camisetas/products/24595-love-tee-ss20-greymelange'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

def check_price(): 
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", class_="ProductMeta__Title Heading u-h2 prodform-title-custom").get_text()
    price = soup.find("span", class_="ProductMeta__Price Price Price--highlight Text--subdued u-h4").get_text()

    converted_price = float(price[1:3])

    print(title.strip())
    print(converted_price)

    if (converted_price < 25):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo

    server.login('your incoming email address', 'your email password (made with google app passwords)')

    subject = 'Price fell down.'
    body = 'Check the link: https://scalperscompany.com/collections/hombre-nueva-coleccion-camisetas/products/24595-love-tee-ss20-greymelange'
    
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'your incoming email address',
        'your destination email address',
        msg
    )

    print('Email has been sent.')
    server.quit

check_price()


    