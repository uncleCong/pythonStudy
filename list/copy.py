my = ["rice","fish","noodle"]
his = my[:]
print(my)
print(his)
print("\n")

my.append("humburger")
his.append("egg")
print(my)
print(his)

print("the top three is" + str(my[:3]))
print("the last three is" + str(his[-3:]))