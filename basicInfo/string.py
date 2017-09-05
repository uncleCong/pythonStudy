a = "wang"

b = "ling"

c = "cong"

print(a)
print(b)
print(c)

d = a+" "+b+" "+c

print(d)
print(d.title()) #首字母大写
print(d.upper()) #全部转换成大写
print(d.lower()) #全部小写
print("\t"+a)	 #添加制表符
print("\nwang\nling\ncong") #添加换行符

e = " man "

print(e.rstrip()) #去除结尾空格
print(e.lstrip()) #去除开头空格
print(e.strip()) #去除两端空格
print(e)

e = e.strip()
print(e)

f = 'this is "wanglingcong"'
print(f)