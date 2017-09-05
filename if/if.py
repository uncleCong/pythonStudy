answer_list = {}
active = True

while active:
	name = input("what's your name: ") 
	site = input("where would you like to go : ")
	answer_list[name] = site

	is_go = input("go on? yes or no")

	if is_go == "no":
		active = False

print(answer_list)