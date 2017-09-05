def make_pizza(size,*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a "+str(size)+"-inch pizza with the following toppings")
	for topping in toppings:
		print("-" + topping)

def get_money(*moneys):
	list = []
	for money in moneys:
		list.append(money)
	return list