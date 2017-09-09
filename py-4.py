import urllib.request
import re

base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "8022"

while nothing:
	content = urllib.request.urlopen(base + nothing).read()
	nextNothing = ''.join(re.findall(r'[0-9]',str(content)))
	nothing = nextNothing
	print(nextNothing)