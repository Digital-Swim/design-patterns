from typing import Dict, Any
user: Dict[str, Any] = {}
a = user.get("a")
print(a)


add = lambda a,b : a+b
print(add(2,3))

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
for i, fruit in enumerate(fruits):
    print(i, fruit)


for i in range(5):
    print(i)


i = 0
while i < 5:
    i = i + 1
    print(i)
    

numbers = [1, 2, 3, 4, 5]
squredNumbers = [x**2 for x in numbers]
print(squredNumbers)

evenNumbers = [x for x in numbers if x%2 == 0]
print(evenNumbers)

table = [[i*j for i in range(1,11)] for j in range(1,3)]
print(table)