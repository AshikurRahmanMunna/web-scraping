import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"

r = requests.get(url)

soup = BeautifulSoup(r.text, features="html.parser")

table = soup.find(
    "table", id="main_table_countries_today")

headers = [h.text.strip() for h in table.find_all(
    "th")]
rows_html = [r for r in table.find("tbody").find_all("tr")[8:]]
stats = []
df = pd.DataFrame(columns=headers)

for row in rows_html:
    data = [d.text for d in row.find_all("td")]
    l = len(df)
    df.loc[l] = data

df.to_csv("corona_stats_countries.csv")
