import functions

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I am {self.name}, {self.age} years old."

alice = Person("Alice", 25)
print(alice.greet())


print(functions.add(1,2))