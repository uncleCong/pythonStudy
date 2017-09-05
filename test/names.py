from test import get_formatted_name
while True:
	first = input("Enter your first name : ")
	if first == "q":
		break
	last = input("Enter your last name : ")
	if last == "q":
		break
	formattd_name = get_formatted_name(first,last)
	print(formattd_name)