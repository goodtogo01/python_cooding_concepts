# # Exercise 1A: Create a string made of the first, middle and last character
# def ll():
#     m = input("Enter your string: ")
#     c = m[0::2]
#     return c
# # print('Here is your string : ',ll(), end=" ")
#
# # Exercise 1B: Create a string made of the middle three characters
# def mm():
#     m = input("Enter your string: ")
#     l = len(m)//2
#     c = m[l-1:l+2]
#     return c
# # print("he : ", mm())
# # Exercise 2: Append new string in the middle of a given string
# s1 = "AE"
# s2 = "BCD"
#
# def tc(a, b):
#     # l = len(a)//2
#     m = a[:1]+b+a[-1:]
#     return m
# # print(tc(s1, s2))
# # Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# def to():
#     m = input("Enter your str : ")
#     c = m[0::2]
#     return c
# # print("Here you go : ", to())
# # Exercise 4: Arrange string characters such that lowercase letters should come first
# s = "abcdefGHIJKL"
# l =[]
# u=[]
# for i in s:
#     if i.islower():
#         l.append(i)
#     else:
#         u.append(i)
# res = "".join(l+u)
# # print(res)
# # Exercise 5: Count all letters, digits, and special symbols from a given string
# m = "ABCDefgh1234!@#$.,]["
#
# dig = ""
# alf = ""
# num = ""
#
# for i in m:
#     if i.isdigit():
#         dig = dig+i
#     elif i.isalpha():
#         alf = alf+i
#     else:
#         num = num+i
# print("Dig : ", dig, "\nAlf : ",alf, "\nNum :", num)


# Exercise 6: Create a mixed String using the following rules
m = "1234567@#$%^&FGHJ34%678"
dig=""
alphas = ""
num = ""
r = ""
f = ""
for i in m:
    if i.isidentifier():
        f += i
    elif i.isdigit():
        dig +=i
    elif i.isnumeric():
        num +=i
    else:
        r +=i
print("Dig : ", dig, "\nAlf : ",alphas, "\nNum :", num, "\nRest of : ", r, "\nf",f)

m = 'ABCfsldfDEdfueiuUILT'
l =''
u =''
for i in m:
    if i.islower():
        l +=i
    else:
        u +=i
print("\nLower : ", sorted(l), ",\nUpper : ",sorted(u))