
print("Dynamically typed and stron typed, once a type is defined can not perform ")
x = 10
y = 10.0

name = "Alice"
name = 1 #valid 

# strongType = name + y   # Not valid  

print(name)

#list 
list = [1,2,3,4,5] #mutable
print(list)
# Tuple
tuple = ("a",  "b", "c")

a, b, c = tuple

print(a)
print(tuple[0])
# Dictionary 
dict = { "name":"ranjit", "age" : 30 }

print(dict["age"])
