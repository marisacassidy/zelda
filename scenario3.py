# Import libraries
import requests
from bs4 import BeautifulSoup

# Specify target url
URL = "https://website.com/release/2/"

# Select user agent: https://deviceatlas.com/blog/list-of-user-agent-strings
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
r = requests.get(url=URL, headers=headers)
# print(r.content)

# Parse html content
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

# Extract all urls in <a> tags in a <div> with a specific class
urls = []

# In line 21, modify _class="..." with your desired div class
for data in soup.findAll('div', class_="txt"):
    link = data.find('a')
    try:
      if 'href' in link.attrs:
        url = link.get('href')
        urls.append(url)
    except:
      pass
  
for url in urls:
  print(url)
