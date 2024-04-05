# todo Exercise 1A: Create a string made of the first, middle and last character
import collections
import json
import re
import string

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
l = []
u = []
for i in s:
    if i.islower():
        l.append(i)
    else:
        u.append(i)
res = " ".join(l + u)
print(f"Lower is come first from {s} : ", res)


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
print("Here is total elements of counts : ", json.dumps(f, indent=2))
print('\nMethod 2: ')

alpha = 0
digit = 0
symbol = 0
for i in s:
    if i.isalpha():
        alpha = alpha + 1
    elif i.isdigit():
        digit = digit + 1
    else:
        symbol = symbol + 1
print("Alpha : ", alpha, "\nDigits : ", digit, "\nSymble : ", symbol)

# todo Exercise 6: Create a mixed String using the following rules
print('\nExercise 6: Create a mixed String using the following rules')
a = 'ABC'
b = 'XYZ'
s3 = " "

for i in range(len(a)):
    s3 = s3 + a[i]
    s3 = s3 + b[-1 - i]
print("Method 1 : ", s3)


def mixchars(a, b):
    s = " "
    for i in range(len(a)):
        s = s + a[i]
        s = s + b[-1 - i]
    return s


print('Method 2: ', mixchars(a, b))

# todo Exercise 7: String characters balance Test
print('\nExercise 7: String characters balance Test')
def bal_chk(a, b):
    flag = True
    for i in a:
        if i in b:
            continue
        else:
            flag = False
    return flag

# case 1:
s1 = "Yn"
s2 = "PYnative"
print("Case 1: ", bal_chk(s1, s2))
# case 2:
s1 = "Ynf"
s2 = "PYnative"
print("Case 2: ", bal_chk(s1, s2))

# todo Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
print('\nExercise 8: Find all occurrences of a substring in a given string by ignoring the case')
'''Write a program to find all occurrences of “USA” in a given string ignoring the case.'''

str1 = "Welcome to USA. usa awesome, isn't it?"
sub_str="USA"
temp_str = sub_str.lower()
c = temp_str.count(sub_str.lower())
print(c)

# todo Exercise 9: Calculate the sum and average of the digits present in a string
print('\nExercise 9: Calculate the sum and average of the digits present in a string')
main_str = "PYnative29@#8496"
dig = 0
sum_dig =0
for i in main_str:
    if i.isdigit():
        dig +=int(i)
        sum_dig +=1
avg = dig/sum_dig
print("Total Digit : ",dig, "\nSum of Dig : ",sum_dig, "\nAvg : ",avg)


# todo Exercise 10: Write a program to count occurrences of all characters within a string
print('\nExercise 10: Write a program to count occurrences of all characters within a string')
str1 = "Welcome to USA"
final_string = collections.Counter(str1)
print("Number of occurrence : ", sorted(final_string))

# todo Exercise 11: Reverse a given string
print('\nExercise 11: Reverse a given string')
str1 = "Welcome to USA"
rev = str1[::-1]
print(rev)
# todo Exercise 12: Find the last position of a given substring
'''rfind() function used to find last indexed place of sub or given string'''
print('\nExercise 12: Find the last position of a given substring')
s1 = "Emma is a data scientist who knows Python. Emma works at google."
sub_str = "Emma"
ff = s1.rfind(sub_str)
print(f"Last position of [{sub_str}] at : ",ff)

# todo Exercise 13: Split a string on hyphens
print('\nExercise 13: Split a string on hyphens')
s ='Emma-is-a-data-scientist'
sub_str = s.split("-")

for i in sub_str:
    print(i)
# todo Exercise 14: Remove empty strings from a list of strings
print('\nExercise 14: Remove empty strings from a list of strings')
s = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("Original String : ", s)
final_list = []
for i in s:
    if i:
        final_list.append(i)
print("Method : 1 \nAfter removing Empty string : ", final_list)

n =list(filter(None, s))
print("Method : 2 \nAfter removing Empty string : ",n)

# todo Exercise 15: Remove special symbols / punctuation from a string
print('\nExercise 15: Remove special symbols / punctuation from a string')
ss = "/*Jon is @developer & musician"
print("Original string is ", ss)
m = ss.translate(str.maketrans('', '', string.punctuation))
print("After removing special chars : ", m)
f = re.sub(r'[\s\w]', '', ss)
print(f)
# res = re.sub(r'[^\w\s]', '', str1)



# todo Exercise 16: Removal all characters from a string except integers
print('\nExercise 16: Removal all characters from a string except integers')
str1 = 'I am 25 years and 10 months old'
mm = ""
for i in str1:
    if i.isdigit():
        mm +=i
print("Method 1 : ",mm)
res = "".join([i for i in str1 if i.isdigit()])
print("Method 2 : ", res)

# todo Exercise 17: Find words with both alphabets and numbers
print('\nExercise 17: Find words with both alphabets and numbers')
s3 = "Emma25 is Data scientist50 and AI Expert"
r = []
temp = s3.split()
for i in s3.split():
    if any(c.isalpha() for c in i) and any(c.isdigit() for c in i):
        r.append(i)
for j in r:
    print(j)
# todo Exercise 18: Replace each special symbol with # in the following string
print('Exercise 18: Replace each special symbol with # in the following string')
s = "Bangladesh$$@@"
print("Before updating : ", s)
r = "#"
for i in string.punctuation:
    s = s.replace(i, r)
print("After Updating : ",s)

