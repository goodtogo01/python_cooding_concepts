# Exercise 7: String characters balance Test
import collections
import json
import re
import string

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
main = "Welcome to USA. usa is a nice usa country."
si="USA"
ff = main.lower().count(si.lower())
print(f"\nTotal {si} occurres of",  ff, " Times")
# Exercise 10: Write a program to count occurrences of all characters within a string
all = "Welcome to USA. usa is a nice usa country."
sg = collections.Counter(all)
print("Total numbe of chars in counts are : ",json.dumps(sg, indent=3))
# Exercise 11: Reverse a given string
fol = "Welcome to USA. usa is a nice use country."
print('\noriginal string : ', fol)
rev = fol[::-1]
rev2 = "".join(reversed(fol))
print("To Reverse: ", rev2)
# Exercise 12: Find the last position of a given substring
ls = "Welcome to USA. usa is a nice usa country."
m = "USA"

cf = ls.lower().count(m.lower())
print(f"\nTotal {m} occurres of",  cf, " Times")

# Exercise 13: Split a string on hyphens
sc = "Welcome-to-USA. usa is a-nice-use-country."
f = re.sub(r'[^\w\s]', " ", sc)
print(f)
# Exercise 14: Remove empty strings from a list of strings
lst = ['al', 1,2,1,5,4,6,2, '', '', 'kazol']
m = list(filter(None, lst))

print("\nAfter removing of space and None : ",m)
# Exercise 15: Remove special symbols / punctuation from a string
chk = "Welcome to USA 215.$%^&"
print("\nOriginal string : ", chk)
f = re.sub(r'[^\s\w]', "", chk)
print("After removing of special chars : ",f)
# Exercise 16: Removal all characters from a string except integers
lpl = "Welcome to 123 USA. 784 usa 45 is a nice use country."
print("\nOriginal string : ", lpl)
c = re.sub(r'[^\d]', " ", lpl) # using reguer expression
print("Olnly Number left : ",c)
# Exercise 17: Find words with both alphabets and numbers
chk = "Welcome to USA215. usa254 is 232a ni232ce country123. $% y7 78787 "
f = re.sub(r'[^\d]', " ", chk) # Only number from the string

def alp_dig(a):
    n =[]
    temp = a.split()

    for i in temp:
        if any(char.isalpha() for char in i) and any (char.isdigit() for char in i):
            n.append(i)
    return n
print("\n",alp_dig(chk))

# Exercise 18: Replace each special symbol with # in the following string
