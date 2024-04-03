import collections
import re

# Exercise 1A: Create a string made of the first, middle and last character
# Exercise 1B: Create a string made of the middle three characters
# Exercise 2: Append new string in the middle of a given string
# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# Exercise 4: Arrange string characters such that lowercase letters should come first
# Exercise 5: Count all letters, digits, and special symbols from a given string
# Exercise 6: Create a mixed String using the following rules
s1 = "Abc"
s2 = "Xyz"
s3 = " "
for i in range(len(s1)):
    s3 = s3 + s1[i]
    s3 = s3 + s2[-1-i]
print(s3)


# print(s3)
# # Exercise 7: String characters balance Test
# def cb(a, b):
#     flag = True
#     for i in a:
#         if i in b:
#             continue
#         else:
#             flag = False
#     return flag
# x = "Py"
# y = "Python"
# print(cb(x, y))
# x = "Pyf"
# y = "Python"
# print(cb(x, y))
#
#
# # Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# str1 = "Emma is a data scientist and emma EmmA, eMmA knows Python. Emma works at google."
# gs = "Emma"
# f = str1.lower().count(gs.lower())
# print(f"Total number of occurrence of {gs} is : ",f," Times.")
# # Exercise 9: Calculate the sum and average of the digits present in a string
# str1 = "PYnative29@#8496"
# dig = 0
# sum_dig = 0
#
# for i in str1:
#     if i.isdigit():
#         dig += int(i)
#         sum_dig +=1
#
# avg  = dig / sum_dig
# print("\nDigits = ", dig, "\nSum = ", sum_dig, "\nAvg = ", avg)
# # Exercise 10: Write a program to count occurrences of all characters within a string
# s = "Apple"
# f = collections.Counter(s)
# print("\nOccurrance : ", f)
# # Exercise 11: Reverse a given string
# s = "Apple"
# print("\n", s[::-1])
#
#
# def ll(a):
#     m = "".join(reversed(a))
#     print(m)
#
#
# ll(s)
# # Exercise 12: Find the last position of a given substring
# """Write a program to find the last position of a substring “Emma” in a given string."""
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# gs = "Emma"
# mm = str1.rfind(gs)
# cc = str1.find(gs)
# print("\nUsing find() method : ", cc)
# print(f"Index position of {gs} at : ", mm)
# # Exercise 13: Split a string on hyphens
# str1 = 'Emma-is-a-data-scientist'
# print("\nOriginal String with HyPhens : ", str1)
# res = re.sub(r'[^\w\s]', '  ', str1)
# print("Method 1 : ", res)
# print("Method 2 : ")
# sp = str1.split("-")
# for i in sp:
#     print(i)
# # Exercise 14: Remove empty strings from a list of strings
#
# o = ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
# print('\nOriginal list of sting : ', o)
# t = list(filter(None, o))
# print("After removing : ", t)
# # Exercise 15: Remove special symbols / punctuation from a string
#
# str1 = "/*Jon is @developer & musician"
# print("\nOriginal string is : ", str1)
# res = re.sub(r'[^\w\s]', '', str1)
# print(res)
#
# # Exercise 16: Removal all characters from a string except integers
# s = "Mono 1 2 is a good man 2 1"
# tem = s.split()
# a = ""
# n = ""
# r = "".join(i for i in s if i.isdigit())
# print('\n', r)
# for i in tem:
#     if i.isalpha():
#         a += i
#     else:
#         n += i
#
# print(n)
#
# # Exercise 17: Find words with both alphabets and numbers
# s = "Mono12 is a good man21"
# re = []
# temp = s.split()
#
# for item in temp:
#     if any(n.isalpha() for n in item) and any(n.isdigit() for n in item):
#         re.append(item)
#
# for i in re:
#     print(i)
#
# # Exercise 18: Replace each special symbol with # in the following string
# import string
#
# mm = "ABCDEFGH2345*&^%$"
# for i in string.punctuation:
#     mm = mm.replace(i, "#")
# print(mm)
