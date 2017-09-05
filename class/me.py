import string
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
intab = string.ascii_lowercase
outtab = string.ascii_lowercase[2:]+string.ascii_lowercase[:2]
table = text.maketrans(intab,outtab) #建立映射关系
print(text.translate(table) ) #翻译字符串，得到提示信息