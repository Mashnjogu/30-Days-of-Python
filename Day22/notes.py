import requests
from bs4 import BeautifulSoup

url  = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
tables = soup.find_all('table', {'cellpadding':'3'})

print(tables)
print(soup.title)
print(soup.title.get_text())
