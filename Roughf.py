import collections
import json

#
#
# def mms():
#     s = str(input("Enter words : "))
#     rev = "".join(reversed(s))
#     if (s == rev):
#         print(f"{s} This is a palindrom. ")
#     else:
#         print(f"{s} is not a palindrom")
#     return rev
#
#
# def mmi():
#     i = int(input("Enter number : "))
#     s = str(i)
#     s = "".join(reversed(s))
#     rev = int(s)
#
#     if (i == rev):
#         print(f"{i} is a palindrom.")
#     else:
#         print(f"{i} is not a plindrom")
#
#
# def fa(m):
#     if m == 0:
#         return 1
#     return m * fa(m - 1)
#
#
# l = [12, 2, 3, 4, 5]
#
#
# # print("Actual List : ", l)
#
#
# def lst(number, n):
#     number.sort()
#     return number[-n]
#
#
# #
# # t = lst(l, 1)
# # print("Sorted List : ", l)
# # print("Largest Number : ", t)
# # print("Smallest number : ", l[0])
# # print("Second highest Number : ", lst(l, 2))
#
# def revStr():
#     s = str(input("Enter your string: "))
#     rev = "".join(reversed(s))
#     return rev
#
#
# # print("Revers String is : ", revStr())
# # string = """Actual List order List Actual order installed"""
#
#
# # print("Skip Duplicates : ", list(set(s)))
# # print("\nEntire String  : ", json.dumps(s, indent=4))
# # mms()
# # mmi()
# # print("factorial : ", fa(10), end="")
#
# # Replace keys 'available' instead of 'installed'
# f = {
#     "Actual": 2,
#     "List": 2,
#     "installed": 1,
#     "order": 2,
#     "not_installed": 1
# }
# m = {key.replace('available', 'installed'): value for key, value in f.items()}
# # f['available']=f.pop('installed') # new value old value
# print("Replace keys : ", json.dumps(m, indent=4))
# # Count the words from string
# string = """Actual List order List Actual Actual Actual Actual  Actual order installed"""
# t = {key: string.count(key)
#      for key in string.split()}
# print("Count words fro string : ", json.dumps(t, indent=4))
#
#
# def top(m):
#     c = "".join(reversed(m))
#     return c
#
#
# def lok(tt):
#     m =[]
#     t = 'A'
#     for i in tt:
#         if i == t:
#             m.append(i)
#     print(f"Total number of {t} is : ",len(m))
#     return m
#
#
# print(lok(string))
# print(top(string))
#
# numberOfWords = collections.Counter(string)
# print("Number of words : ", json.dumps(numberOfWords, indent=4))
#
# numberOfActualWords = string.count('Actual')
# print("Number of Actual is : ", numberOfActualWords)
#
# rev = string[::-1]
# print(rev)
#
# t = (9,2,8,1,3,7)
# rev2 = t[::-1]
# print(rev2)
#
keys = ["One", "Two", "Three"]
values = [1, 2, 3]
# df = dict(zip(keys, values))
# print(df)

# # merge two dic
# dic1 = {'One': 1, 'Two': 2, 'Three': 3}
# dic2 = {'Three': 3, 'four': 4, 'Five': 5}
# dic3 = {**dic1, **dic2}
# print("Merged dictionaries with dict view: ", dict(dic3, indent=3))
# print("\nMerged dictionaries with json view : ", json.dumps(dic3, indent=3))

sample_dict = {
    "name": ['kamal', 'jamal', 'malamal'],
    "id": [10, 11, 12],
    "age": [25, 70, 89],
    "salary": [12344, 5475, 8000, ],
    "city": ['NY', 'PA', 'NJ']
}

# Keys to extract
keys = ['id', 'city']
# print(keys)
# print(dict(sample_dict))
# new_dict = {k: sample_dict[k] for k in keys}
# print(new_dict)

res = dict()
for k in keys:
        res = ({k: sample_dict[k]})
        print(res)
# print(res)