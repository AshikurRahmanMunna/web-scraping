import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get(
    "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
soup = BeautifulSoup(response.text, features="html.parser")
products_elem = soup.find_all("div", {"class": "thumbnail"})
products = []
for product_elem in products_elem:
    img = product_elem.img.attrs["src"]
    price = product_elem.find("h4", {"class": "price"}).text
    title = product_elem.find("a", {"class": "title"}).text
    description = product_elem.find("p", {"class": "description"}).text
    reviews = product_elem.find(
        "div", {"class": "ratings"}).find("p", {"class": "pull-right"}).text
    obj = {'img': img, 'price': price,
           'title': title, 'description': description, "reviews": reviews}
    products.append(obj)

df = pd.DataFrame(products)
df.to_excel("product_details.xlsx")
