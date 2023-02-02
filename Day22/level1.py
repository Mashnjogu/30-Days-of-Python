import requests
from bs4 import BeautifulSoup

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
# print(soup)

data = {}

for tr in soup.findAll('tr'):
    key = tr.find('td', class_= 'fact-label').text.strip()
    value = tr.find('td', class_='fact-value').text.strip()
    data[key] = value

print(data)
