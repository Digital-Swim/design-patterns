import gc
import tracemalloc
import sys

print("=== Python Memory Management Demo ===\n")

# -------------------------------
# 1. Reference Counting
# -------------------------------
print("1. Reference Counting Example")
a = [1, 2, 3]
b = a  # Reference count increases
print("Reference count of 'a':", sys.getrefcount(a))  # extra +1 due to getrefcount argument
del a
print("Reference count of 'b':", sys.getrefcount(b))
del b
print("All references deleted\n")

# -------------------------------
# 2. Garbage Collection & Circular References
# -------------------------------
print("2. Circular Reference Example")

class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

node1 = Node("node1")
node2 = Node("node2")

node1.ref = node2
node2.ref = node1

print("Deleted node1 and node2")
del node1
del node2

print("Garbage collector collects unreachable objects:", gc.collect(), "\n")

# -------------------------------
# 3. Memory Leak Example
# -------------------------------
print("3. Memory Leak Simulation")

leaky_list = []

def create_leak():
    temp_list = [i for i in range(10000)]
    leaky_list.append(temp_list)

for _ in range(5):
    create_leak()

print("Leaky list size:", len(leaky_list))

del leaky_list
gc.collect()
print("Memory reclaimed after deleting leaky_list\n")

# -------------------------------
# 4. Using __slots__ to Save Memory
# -------------------------------
print("4. Using __slots__")

class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj1 = WithoutSlots(1, 2)
obj2 = WithSlots(1, 2)

print("Size of object without slots:", sys.getsizeof(obj1))
print("Size of object with slots:", sys.getsizeof(obj2), "\n")

# -------------------------------
# 5. Generators vs Lists
# -------------------------------
print("5. Generators vs Lists Memory Usage")

def list_generator(n):
    return [i for i in range(n)]

def real_generator(n):
    for i in range(n):
        yield i

list_obj = list_generator(1000000)
gen_obj = real_generator(1000000)

print("Size of list with 1M items:", sys.getsizeof(list_obj))
print("Size of generator with 1M items:", sys.getsizeof(gen_obj), "\n")

# -------------------------------
# 6. Using tracemalloc
# -------------------------------
print("6. Tracking Memory with tracemalloc")
tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()
big_list = [i * 2 for i in range(100000)]
snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')
print("Top memory differences:")
for stat in top_stats[:3]:
    print(stat)

tracemalloc.stop()

print("\n=== End of Demo ===")
