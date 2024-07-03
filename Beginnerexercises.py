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
# ----------------------------- 
# Classes and objects
# 1. Take input from user(n,a,g)
# 2. Create a class with init method and also create a action method display to print attributes
# 3. Also try to use arguemnts and parters with different objects


# n = input("Name: ")
# a = int(input("Age: "))
# g = int(input("Grades: "))

# class User:
#    def __init__(self, n, a, *g):
#      self.n = n
#      self.a = a
#      self.g = g
     
#    def Display(self):
#      print("\nName:", self.n)
#      print("Age:", self.a)
#      print("Grades:", self.g)
     
     
# user1 = User("Mejra", 19, 8, 9, 10, 10)


# user2 = User("Ena", 22, 10, 10, 10, 10)

# user1.Display()
# user2.Display()
# ----------------------------- 
# Make a simple calculator app using path

# from calc import calculate 

# def calculator():
#   a = int(input("Enter number 1: "))
#   b = int(input("Enter number 2: "))
#   c = input("Enter type of calculation (+, -, *, /): ")
  
#   if (c == "+"):
#     calculate.add(a, b)
    
#   if (c == "-"):
#     calculate.subtract(a, b)
    
#   if (c == "*"):
#     calculate.multiply(a, b)
    
#   if (c == "/"):
#     calculate.divide(a, b)
  
# calculator()

# ----------------------------- 
# 169. Majority Element

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# class Solution(object):
#     def majorityElement(self, nums):
#         counts = {}
        
#         for i in nums:
#             if i in counts:
#                 counts[i] += 1
#             else: counts[i] = 1
            
#             maxCount = 0
#             maj = None
            
#             for i, count in counts.items():
#                   if (count > maxCount):
#                       maj = i
#                       maxCount = count
                      
#         return maj
                
# s1 = Solution()
# nums = [1,1,2,3,4,5,6,7,7,3,7]
# print(s1.majorityElement(nums))
            
# ----------------------------- 

# 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution(object):
    def removeDuplicates(self, nums):
        # nums = [1,2,3,1,4,5]
        
        counter = {}
        repeatedNum = None
        
        length = len(nums)
        
        
        for i in list(nums):
            if i in counter:
                counter[i] += 1
                nums.remove(i)
            else: counter[i] = 0
            
        maxCount = 0
        
        for i, repeats in counter.items():
            if repeats > maxCount:
                maxCount == counter
                repeatedNum = counter[i]
                
        print(nums)
        
            
            
s1 = Solution()

s1.removeDuplicates([0,0,1,1,1,2,2,3,3,4])  

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).