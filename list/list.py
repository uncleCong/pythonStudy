animals = ["dog","pig","cat"]

print(animals)
print(animals[0])
print(animals[-1])
print(animals[0].upper()+'\n------------------')

#修改
animals[0] = "tiger"
print(animals[0]+'\n-----------------')

#增加
animals.append("rabbit")
animals.insert(0,'elephant')

print(animals)
print("-------------------")

#删除
del animals[0]
print(animals)
pop_ele = animals.pop()
pop_f_ele = animals.pop(0)
print(pop_f_ele)
print(pop_ele)
print(animals)

animals.remove("cat")

print(animals)


