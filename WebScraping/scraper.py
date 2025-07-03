import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = 'https://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Books Data Scrape Kar Rahe
books = soup.find_all('article', class_='product_pod')

data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text.strip()
    rating = book.p['class'][1]  # Star rating (example: 'Three')
    data.append({'Title': title, 'Price': price, 'Rating': rating})

# Excel File Me Save Kar Rahe
df = pd.DataFrame(data)
df.to_excel('books.xlsx', index=False)

print("✅ Data Saved Successfully to books.xlsx")
