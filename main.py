from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6", headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10" ,"Accept-Language":"en-US" })
soup=BeautifulSoup(response.text , "lxml")

title = soup.find(id="productTitle").getText().strip()
price = soup.find(class_="a-price-whole").getText() + soup.find(class_="a-price-fraction").getText()

if price < 100:
    message = f"{title} is no {price}"

    with smtplib.SMTP(YOUR_SMTP_ADRESS,port = 587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL , YOUR_PASSWORD)
        connection.senmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )