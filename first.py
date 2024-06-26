print("Oink")


# print(games[0])

# for i in range(5) :
#     print(games[i])
    
    
# r = range(1, 10, 1)
# q = list(r)
# print(q)

# r2 = list(range(5, 0, -1))
# print(r2)

# -----------------------------

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
# print(stepen)

# -----------------------------

A = [0,1,2,3,4,5] # LIST
B = (0,1,2,3,4,5) # TUPLE
C = {0,1,2,3,4,5} # SET
D = {"Name:": "Mejra", "Age:":19} # DICTIONARY

# print("age" in D)
# print(2 in C)

# for a in A:
#     print(a)

# for i, j in D.items():
#     print(i, j)
    
# for x in range(1, 5):
#     print(x)


# i = 0

# while i < 5:
#     print(i)
#     i+=1
    
# -----------------------------
    
x = "           TLOU"
y = "Before the storm"

# print(x.lower().capitalize())

# print(y.capitalize())

# print(y[0:7] + y[11:16].capitalize()) 

# print(x.lstrip())

# -----------------------------


games = ["TLOU", "TLOU2", "AC ODYSSEY", "AC VALHALLA", "LIS"]

# g1 = games[1]
# print(len(g1))

# games.insert(6, "BEFORE THE STORM")

# games.append("Ghost of Tsushima")

# for i in games:
#     print(i)

# -----------------------------    
    
# books = {"MYORAR": "Odessa M.", "The Idiot":"Fyodor D.", "Pachinko":"Min Ji"}

# books["Normal People"] = "Sally Rooney"

# print(books)

# # -----------------------------    

# def shop(item, price):
#     print("Item: ", item)
#     print("Price: ", price)
    
    
# shop("Choccy", 70)


# def uni(name, major, year, **marks):
    
   
#     print("\nName: ", name)
#     print("Major: ", major)
#     print("Year: ", year)
#     # print("Marks: ", marks)
    
#     for x, y in marks.items():
#         print("Marks: ", x, y)
        
    
    

# uni("Mejra", "CS", 2, math=9, coding=9)

# -----------------------------    

# class Game:
    
#     def __init__(self, name):
#         self.name = name
#         self.year = 2020
#         self.rating = 9.5
        
#     def gameInfo(self):
#         print("Name: ", self.name)
#         print("Year: ", self.year)
#         print("Ratinself: ", self.rating)
        

# game1 = Game("the last of us")

# game1.gameInfo()

# -----------------------------    encapsulation


class TLOU3:
    def __init__(self):
        self.release = 2027
        self.__new_release = 2028
        
    def getNewRelease(self):
        return self.__new_release
    
    def setNewRelease(self, newRelease):
        self.__new_release = newRelease
        
        
i1 = TLOU3()

i1.setNewRelease(2026)

print(i1.getNewRelease())
