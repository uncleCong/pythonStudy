def str_switch(str):
	inTab = ""
	outTab = "yz"
	for i in range(97,123):
		inTab += chr(i)

	for j in range(97,121):
		outTab += chr(j)
	print(inTab)
	print (str.maketrans(inTab,outTab))

print(str_switch("abc"))