# todo Exercise 1A: Create a string made of the first, middle and last character
import collections
import json

print('Exercise 1A: Create a string made of the first, middle and last character')
s = 'zaman'
print("Actual String : ", s)
s2 = s[0::2]
print("first, midle, and last charecters are : ", s2)

# todo Exercise 1B: Create a string made of the middle three characters
print('\nExercise 1B: Create a string made of the middle three characters')
name = 'ABCDEABCD'
print("Actual String : ", name)


def mdlChars(x):
    ln = len(x) // 2
    res = x[ln - 1:ln + 2]
    return res


print("Middle three characters:", mdlChars(name))

# todo Exercise 2: Append new string in the middle of a given string
print('\nExercise 2: Append new string in the middle of a given string')
a = 'ABCD'
b = 'OO'


def mixStr(x, y):
    le = len(x) // 2
    results = x[:le] + y + x[le:]
    return results


print(f"Concatinate with {a} and {b} as :", mixStr(a, b))

# todo Exercise 3: Create a new string made of the first, middle, and last characters of each input string
print('\nExercise 3: Create a new string made of the first, middle, and last characters of each input string')
s = 'ABCDE'


def final_str(s):
    res = s[0::2]
    return res


print(f'first, middle, and last characters of given string as {s} :', final_str(s))

# todo Exercise 4: Arrange string characters such that lowercase letters should come first
print('\nExercise 4: Arrange string characters such that lowercase letters should come first')
s = 'abcdABCD'
l=[]
u=[]
for i in s:
    if i.islower():
     l.append(i)
    else:
       u.append(i)
res = " ".join(l+u)
print(f"Lower is come first from {s} : ",res)

def lower_and_upper_check(m):  # only lower or uppder case
    lo = []
    up = []
    for i in str(m):
        if i.islower():  # for upper case i.isupper()
            lo.append(i)
        else:
            up.append(i)
    return lo

# TODO Exercise 5: Count all letters, , and special symbols from a given string
print('\nExercise 5: Count all letters, , and special symbols from a given string')
s = "Welcom 123@#$%> '' "
f = collections.Counter(s)
print("Here is total elements of counts : ",  json.dumps(f, indent=2))
print('\nMethod 2: ')

alpha =0
digit = 0
symbol = 0
for i in s:
    if i.isalpha():
        alpha = alpha+1
    elif i.isdigit():
        digit = digit + 1
    else:
        symbol = symbol+1
print("Alpha : ",alpha, "\nDigits : ",digit,"\nSymble : ",symbol)



# todo Exercise 6: Create a mixed String using the following rules
print('\nExercise 6: Create a mixed String using the following rules')
a = 'ABC'
b = 'XYZ'
s3 = " "

for i in range(len(a)):
    s3 = s3 +a[i]
    s3 = s3+b[-1-i]
print("Method 1 : ",s3)

def mixchars(a,b):
    s = " "
    for i in range(len(a)):
        s = s+a[i]
        s = s+b[-1-i]
    return s

print('Method 2: ',mixchars(a, b))

# Exercise 7: String characters balance Test

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Exercise 9: Calculate the sum and average of the digits present in a string
# Exercise 10: Write a program to count occurrences of all characters within a string
# Exercise 11: Reverse a given string
# Exercise 12: Find the last position of a given substring
# Exercise 13: Split a string on hyphens
# Exercise 14: Remove empty strings from a list of strings
# Exercise 15: Remove special symbols / punctuation from a string
# Exercise 16: Removal all characters from a string except integers
# Exercise 17: Find words with both alphabets and numbers
# Exercise 18: Replace each special symbol with # in the following string

# 100335
