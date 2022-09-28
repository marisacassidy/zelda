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

# Extract all urls in <a> tags with a specific class
# Modify the a tag class in line 19
for link in soup.find_all('a', class_="whatever"):
  print(link.get('href'))
