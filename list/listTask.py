person = ["feng","chen","zhang"]

message = " join my party"

print(person[0]+message)
print(person[1]+message)
print(person[2]+message)

person_cannot_join = person.pop()
print(person_cannot_join + " can't join")

person.append("guo")
print(person);

person.insert(0,"qi")
print(person)

p1 = person.pop()
print("sorry " + p1)

p2 = person.pop()
print("sorry " + p2)

print(person)

person.sort();
print(person)
person.sort(reverse = True)
print(person)

new = [1,2,3,4,5]
new.reverse();
print(new)

print(len(new))

word = ['a','b','d','c']
print(sorted(word))
print(word)
