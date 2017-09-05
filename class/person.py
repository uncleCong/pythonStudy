class Father():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def describe(self):
		print("i am "+str(self.age)+" years old and my name is "+self.name)

class Work():
	def __init__(self,place,money):
		self.place = place
		self.money = money
	def work_info(self):
		print("i work in "+self.place+" i earn "+str(self.money))

class Me(Father):
	def __init__(self,name,age,place,money):
		super().__init__(name,age)
		self.work = Work(place,money)

m = Me("wanglingcong","18","beijing","10000")

m.describe()
