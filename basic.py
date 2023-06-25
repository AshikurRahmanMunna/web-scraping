import requests
from bs4 import BeautifulSoup

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
    obj = {'img': img, 'price': price,
           'title': title, 'description': description}
    products.append(obj)

print(products)
