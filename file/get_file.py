#encoding:UTF-8  
import urllib.request

response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()

with open("url.txt","w") as file_object:
	file_object.write(str(response))
