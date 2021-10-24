from os import urandom
from bs4 import BeautifulSoup
import requests

url = ('https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1')

r = requests.get(url)

web_content = BeautifulSoup(r.text, 'lxml')

web_content = web_content.find_all('path')

for path in web_content:
    number = path.find()
    print(path)

# print(web_content)