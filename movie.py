import urllib.request
import requests
from bs4 import BeautifulSoup

session = requests.Session()
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
session.get('http://maoyan.com')

base_url = "http://maoyan.com/board/4?offset="
base_count = 10
page_num = 0
rank = 1

while page_num < 10:
	open_url = base_url + str(base_count*page_num)
	print("--------正在抓取猫眼电影排行榜第"+str(page_num+1)+"页--------")
	page_num += 1
	html = urllib.request.urlopen(open_url).read()
	soup = BeautifulSoup(html,"html.parser")
	for name in soup.find_all("div",class_="movie-item-info"):
		print("第"+str(rank)+"名"+name.a.text)
		detail_url = name.a.get("href")
		detail = session.get("http://maoyan.com/"+detail_url).text
		print(detail)
		detail_soup = BeautifulSoup(detail,"html.parser")
		detail_content = detail_soup.find("span",class_="dra")
		print(detail_content)
		rank += 1
