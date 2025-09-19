from typing import Dict, Any
import logging
from functools import wraps

user: Dict[str, Any] = {}
a = user.get("a")
#print(a)

# passig mutable parameters for defaults, 

def add_item(item, items = []): # use items = None ,
    items.append(item)
    return items

#print(add_item(1))
#print(add_item(2)) # expeted [2] but got [1,2]

def read_file(path):
    try:
        with open(path,"r") as f:
            return f.read()
    except Exception as e:
        logging.error(f"failed to read file {e}" )
        raise 

#read_file("test.txt")

x = 1
y = 1
#print(x is y)
#print(x == y)

n = [1,2,3,4]
sn = [x**2 for x in n]
f = [x for x in n if x % 2 == 0]
#print(sn, f)

class A: pass
class B(A): pass
class C(B): pass
print(C.mro())


def decorator(func):
    @wraps(func)
    def wrapper(*args):
        print("before call")
        func(*args)
        print("After call")
    return wrapper

@decorator
def say(text:str):
    print("say" + text)
    

say("hello")
print(say.__name__, say.__dict__, say.__doc__)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for n in fib(5):
    print(n)

def read_file(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

for line in read_file("test.txt"):
    print(line)
