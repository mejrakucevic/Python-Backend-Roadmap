# Given two inter numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

a = 10
b = 150

# if ((a*b) < 1000) :
#     print(a*b)
# else: print(a+b)


# ID checking with nested conditionals

# a= int(input("Enter your a: "))

# if (a >= 18):
#     id = input("Do you have ID with you? (Y/N): ")
#     if (id == "Y"):
#         print("Welcome!")
#     else: print("You can't enter without an ID")
    
# else: print("Under 18 not allowed")


# q = input("Enter your n: ")

# if (q == "Mejra"):
#     print("Room A2")
# elif (q == "Ena"):
#     print("Room B66")
# elif (q == "Sara"):
#     print("Room C6")
# else : print("You are not a guest here")

# x = 1

# while x <= 10:
#     print(x)
#     x += 1
# else: print("Loop complete")

# a =float(input("Enter A: "))
# b =float(input("Enter B: "))


# c = input("Enter 1 for sum of A and B, 0 for exit: ")

# while c != '0':
  
#     print(a+b)
  
#     c = input("Enter 1 for sum of A and B, 0 for exit: ")
#     if c != '0':
#       a =float(input("Enter A: "))
#       b =float(input("Enter B: "))
  
# else: print("Exited program")



# Write a function that accepts 2 parters of the s type, it can be a string or float, and adds them tother. If both parters are not the saem type
# give error messa to user

# x= input("Enter the first value: ")
# y = input("Enter the second value: ")

# def errorCheck(x, y):
#   if type(x) == type(y):
#     return x + y
#   else:
#     print("The values must be of the s type")

# result = errorCheck(x,y)
# print(result)

# Classes and objects
# 1. Take input from user(n,a,g)
# 2. Create a class with init method and also create a action method display to print attributes
# 3. Also try to use arguemnts and parters with different objects


# n = input("Name: ")
# a = int(input("Age: "))
# g = int(input("Grades: "))

class User:
   def __init__(self, n, a, *g):
     self.n = n
     self.a = a
     self.g = g
     
   def Display(self):
     print("\nName:", self.n)
     print("Age:", self.a)
     print("Grades:", self.g)
     
     
user1 = User("Mejra", 19, 8, 9, 10, 10)


user2 = User("Ena", 22, 10, 10, 10, 10)

user1.Display()
user2.Display()
