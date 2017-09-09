import urllib.request as get
from bs4 import BeautifulSoup as handle

base_url = "https://movie.douban.com/top250?start="
base_page = 0
page_num = 25

# while base_page < 10:
print(base_url+str(base_page*page_num))
content = get.urlopen(base_url+str(base_page*page_num)).read()

print(str(content))

