import re
import urllib.request

content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()

#条件：One small letter, surrounded by EXACTLY three big bodyguards on each of its sides
#正则：一个小写字母两侧有且只能有三个大写字母，'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
#使用Python的r前缀，不用考虑转义的问题

reg = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
print(''.join(reg.findall(str(content))))
