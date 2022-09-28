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

# Extracting with pagination
# Modify the start page in line 19
page = 1

urls = []

hasNextPage=True

while(hasNextPage):
  r = requests.get(f"https://website.com/release/{page}/").text
  soup = BeautifulSoup(r, 'lxml')
  # Modify the div class in line 29
  website = soup.find_all('div', class_="txt")
  for data in website:
    link = data.find('a')
    try:
      if 'href' in link.attrs:
        url = link.get('href')
        urls.append(url)
    except:
      pass
  
  for url in urls:
    print(url)
    
  print("-- Page ",page," --")

  # Modify the Next button tag type and class
  if soup.find("li",class_='next') is None:
    hasNextPage=False

  page+=1
