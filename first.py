print("Oink")

x=5.34
y=5.5


# print(type(x))

if (x>y):
    print("x is greater than y") 
    
else: print("y is greater than x")
    
    
    
# myName = "Mejra"
# print(myName)

games = ["TLOU", "TLOU2", "AC ODYSSEY", "AC VALHALLA", "LIS"]

# print(games[0])

# for i in range(5) :
#     print(games[i])
    
    
# r = range(1, 10, 1)
# q = list(r)
# print(q)

# r2 = list(range(5, 0, -1))
# print(r2)


# LISTE VS SETS
# Order:

# List: A list is an ordered collection of items. The items have a specific order, and this order will be maintained.
# Set: A set is an unordered collection of unique items. The items do not have a specific order, and duplicates are not allowed.
# Duplicates:

# List: Lists can contain duplicate items.
# Set: Sets cannot contain duplicate items. If you try to add a duplicate item to a set, it will be ignored.
# Mutability:

# List: Lists are mutable, meaning you can change their content (add, remove, or modify items) after they are created.
# Set: Sets are also mutable, but only the individual elements are immutable. You can add or remove items, but you cannot modify an existing item in place.
# Indexing and Slicing:

# List: Lists support indexing and slicing. You can access individual elements or a range of elements using indices.
# Set: Sets do not support indexing or slicing because they are unordered.
# Performance:

# List: Lists are generally slower for membership tests (checking if an item exists) compared to sets.
# Set: Sets are optimized for membership tests and are generally faster than lists for this purpose due to their underlying hash table implementation.
# Common Operations:

# List: Common operations include appending, extending, inserting, removing, and popping elements, as well as concatenation and repetition.
# Set: Common operations include adding, removing, union, intersection, difference, and symmetric difference.

set1 = {17,2,3,4,5,234,756,22}
# print(set1)


# DICTIONARIES : KEY:VALUE PAIRS
dict = {"Lock1":2034,"Lock2":5552}

# print(dict)
# print(dict["Lock1"])


# age = int(input("Age: "))
# print("You are ", age, " years old")

import math

stepen = math.sqrt(64)
print(stepen)