import urllib.request
import pickle

content = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

words = pickle.load(content)

for word in words:
	result = ''.join([x[0]*x[1] for x in word])
	print(result)
