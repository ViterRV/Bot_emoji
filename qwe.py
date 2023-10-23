"""result = (80 - 12*5) / 4
print(result)


print(0xA+0xa)
x= "foo"
print(x+2)"""

"""names1 = ['ruslan','vova','vlad','dima']
names2 = names1
names3=names1[:]

names2[0] = 'alice'
names3[1]='bob'
sum = 0

for ls in (names1, names2, names3):
    if ls[0] == 'alice':
        sum +=1
    if ls[1] == 'bob':
        sum +=10

print(names1)
print(names2)
print(names3)
print(sum)

"""

"""class parent:
    def __init__(self,param):
        self.v1 = param

class child(parent):
    def __init__(self, param):
        self.v2 = param

obj = child(11)
print(obj.v1 + " "+ obj.v2)"""

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def compare_age(self, other):
		if self.age > other.age:
		    return f"{other.name} is younger than me"
		elif self.age < other.age:
		    return f"{other.name} is older than me"
		else:
		     return f"{other.name} is the same age as me"

p1 = Person("Samuel", 54)
p2 = Person("Joel", 36)

result = p2.compare_age(p1)
print(result)