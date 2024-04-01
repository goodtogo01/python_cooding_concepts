# todo Exercise 1A: Create a string made of the first, middle and last character
print('Exercise 1A: Create a string made of the first, middle and last character')
s = 'zaman'
print("Actual String : ", s)
s2 = s[0::2]
print("first, midle, and last charecters are : ",s2)

# todo Exercise 1B: Create a string made of the middle three characters
print('\nExercise 1B: Create a string made of the middle three characters')
name = 'ABCDEABCD'
print("Actual String : ", name)
ln = int(len(name)/2)
f = name[ln-1: ln+2]
print("middle three characters : ",f)
l =int(len(name))

print('Len = ', l, '\nHalf of len = ',round(l/3, None))
cc = name[4::2]
print("cc " , cc)
# res = name[s1-1:s1+2]
print("ffll : ", name[0::2]) # ACE
print("ffll : ", name[1::2]) # BD


# todo Exercise 2: Append new string in the middle of a given string
print('\nExercise 2: Append new string in the middle of a given string')
s1 = 'khosru'
s2 = 'zaman'

m = int(len(s1)/2)
x = s1[:m:]
x = x + s2
x = x + s1[m:]
print(x)



# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# Exercise 4: Arrange string characters such that lowercase letters should come first
# Exercise 5: Count all letters, digits, and special symbols from a given string
# Exercise 6: Create a mixed String using the following rules
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
