import gc
import tracemalloc
import sys

print("=== Circular Reference Memory Leak with tracemalloc ===\n")

class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

# Disable automatic GC to simulate memory leak
gc.disable()

# Start tracking memory
tracemalloc.start()

def memory_snapshot(tag):
    current, peak = tracemalloc.get_traced_memory()
    print(f"{tag}: Current={current / 1024:.2f} KB, Peak={peak / 1024:.2f} KB")

# Step 1: Before creating nodes
memory_snapshot("Before creating nodes")

# Step 2: Create circular reference
node1 = Node("node1")
node2 = Node("node2")
node1.ref = node2
node2.ref = node1

memory_snapshot("After creating circular nodes")

# Step 3: Delete external references
del node1
del node2
memory_snapshot("After deleting external references (cycle exists)")

# Step 4: Manually run garbage collector
unreachable_objects = gc.collect()
memory_snapshot("After gc.collect()")
print(f"Unreachable objects collected by GC: {unreachable_objects}")

# Stop tracemalloc
tracemalloc.stop()

print("\n=== End of Demo ===")
