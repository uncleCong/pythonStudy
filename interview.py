from functools import reduce

a = [1, 2, 3, 4, 5]

print(reduce(lambda x,y:x+y,[a[value]+3 for value in range(0,5) if value%2 == 0]))
