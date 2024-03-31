# Exercise  1:  Reverse  a  list  in  Python
import collections
#
# o = [100, 200, 300, 400, 500]
# # m=o[::-1]
# o.reverse()
# # print(o)
#
# # Exercise  2:  Concatenate  two  lists  index-wise
# # following condition
# # combine / sum of index value
# # keep same index
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# # ['My', 'name', 'is', 'Kelly'] -
# # i+j i+j i+j i+j single iteration
# m = [i+j for i,j in zip(list1, list2)]
# print(m)
#
# # Exercise  4:  Concatenate  two  lists  in  the  following  order
# l1 = ["Hello ", "take "]
# l2 = ["Dear", "Sir"]
# # multi iteration i[0] j[0], i[0] j[1], i[1] j[0], i[1] j[1]
# # out put: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# m2 = [i+j for i in l1 for j in l2]
# print(m2)
# # Exercise  3:  Turn  every  item  of  a  list  into  its  square
# l = [2,4,5,6]
# f =[]
# #  [4, 16, 25, 36]
# for i in l:
#     f.append(i*i)
# print(f)
#
# # Exercise  5:  Iterate  both  lists  simultaneously with reverse order of list2
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# """
# 10 400
# 10 300
# 10 200
# 10 100
# """
# def ll(a, b):
#     for i in a:
#         for j in b[::-1]:
#             print(i, j)
#         break
# ll(list1, list2)
# # Exercise  6:  Remove  empty  strings  from  the  list  of  strings
# li = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# print("Actual list: ", li)
# for i in li:
#     if i == "":
#         li.remove(i)
#
# print(li)
#
# # Exercise  7:  Add  new  item  to  list  after  a  specified  item
# nestedLoop = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# print("\nExercise  7 Original list : ", nestedLoop)
# nestedLoop.insert(3, 11)
# print("Exercise  7 Updated list : ", nestedLoop)
# # Exercise  8:  Extend  nested  list  by  adding  the  sublist
# ml = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# print("\nOriginal list : ", ml)
# sl = [1,2,3]
# ml[2].insert(3, sl)
# print(ml)
#
# # Exercise  9:  Replace  list’s  item  with  new  value  if  found
# # exptd  [5, 10, 15, 1111, 25, 50, 20]
# cl = [5, 10, 15, 20, 25, 50, 20]
# print("\nOriginal list : ", cl)
# indx = cl.index(50)
# cl[5]=91
#
#
# print("After removing 20  : ",cl)
#
#
# # Exercise  10:  Remove  all  occurrences  of  a  specific  item  from  a  list.
# ul = [5, 10, 15, 20, 25, 50, 20]
# print("\nOriginal list : ", ul)
# while 20 in ul:
#     ul.remove(20)
# print("After removing multiple occurance : ", ul)
#
#
# """
# Exercise 9: Replace list’s item with new value if found
# original list :  [5, 10, 15, 20, 25, 50, 20]
# After removing 20 :  [5, 10, 15, 11, 25, 50, 20]
# """
l = {1,1,2,3,4}
m = {1,1,2,5,6}
com = l.union(m) # only common + uncommon items but no duplicate
print("common + uncommon ", com)
fl = l.intersection(m) # only common
print("only common  ", fl)
# print(l.count(1))
tom = l.symmetric_difference(m)

print("Only uncommon: ", tom)
mol = l.difference(m)
print("Different set1 from set2 : ", mol)


flc =[5, 10, 15, 20, 25, 50, 20, 20]

lom = []
m = len(lom)
lom = collections.Counter(flc)
print(f"found {m} in the list around : ", lom , "Times")