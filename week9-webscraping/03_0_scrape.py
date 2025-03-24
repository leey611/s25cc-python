import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Ada_Lovelace")
# print(response.text)

soup = bs4.BeautifulSoup(response.text, "html.parser")
# print(soup)
# print(soup.select(".mw-heading"))

headings = []

for item in soup.select(".mw-heading"):
    headings.append(item.text)

# print(headings)

import pandas as pd
heading_df = pd.DataFrame()
heading_df['headings'] = pd.Series(headings).values
# print(heading_df)
# print(heading_df["headings"].values)

heading_df.to_csv('headings.csv')