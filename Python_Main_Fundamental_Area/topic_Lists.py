des = """
Lists are used to store multiple items in a single variable.

List Items
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value:

"""
print(des)


import math
import collections

# todo find only repeated item from the list
print('Find only repeated item from the list')
flc =[5, 10, 15, 20, 25, 50, 20, 20]
v = 20
print(f"Found {v} in the list of : ",flc.count(20)," Times")

# todo Exercise 1: Reverse a list in Python
print('\nExercise 1: Reverse a list in Python')
list1 = [100, 200, 300, 400, 500]
print('Original List: ', list1)

rev = list1[::-1]  # using split method
print("Reversed with split method : ", rev)
list1.reverse()  # using reverse method
print("Reversed List: ", list1)

# todo Exercise 2: Concatenate two lists index-wise
print('\nExercise 2: Concatenate two lists index-wise')
# single iteration i+j i+j i+j i+j
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3 = [i + j for i, j in zip(list1, list2)]
print(l3)

# todo Exercise 3: Turn every item of a list into its square
print('\n Exercise 3: Turn every item of a list into its square')
numbers = [1, 2, 3, 4, 5, 6, 7]
print("original list : ", numbers)
sqrList = []  # Create empty list for further storage
for i in numbers:
    # Calculate square and add into new list
    sqrList.append(i * i)
print("Square of list :", sqrList)

# todo Exercise 4: Concatenate two lists in the following order
print('\nExercise 4: Concatenate two lists in the following order')
# multi iteration i[0] j[0], i[0] j[1], i[1] j[0], i[1] j[1]
l1 = ["Hello ", "take "]
l2 = ["Dear", "Sir"]
# Expected out put: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list3 = [i + j for i in l1 for j in l2]
print("method 1: ", list3)
t = []
for i in l1:
    for j in l2:
        t.append(i + j)

print("method 2: ", t)
# todo Exercise 5: Iterate both lists simultaneously
#  and second list must reversed
print('\nExercise 5: Iterate both lists simultaneously')
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i, j in zip(list1[::-1], list2):
    print(i, j)
print()

# todo Exercise 6: Remove empty strings from the list of strings
print('\nExercise 6: Remove empty strings from the list of strings')
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print("Actual list: ", list1)
s = []
for i in list1:
    if i == "":
        list1.remove(i)
print("Method 1: After removing empty String : ",list1)
emp = list(filter(None, list1))
print("Method 2: After removing empty String : ",emp)

# todo Exercise 7: Add new item to list after a specified item
print('\nExercise 7: Add new item to list after a specified item')
newVal = 7000
nestedLoop = [10, 20, [300, 400, [5000, 6000, [199]], 500], 30, 40]
print("Original list : ", nestedLoop)
nestedLoop[2][2].append(newVal)
print(f"After Adding {newVal} in particular index:\n",nestedLoop)


# todo Exercise 8: Extend nested list by adding the sublist
print('\nExercise 8: Extend nested list by adding the sublist')
orgList = [10, 20, [300, 400, [5000, 6000, [199], 1587], 500], 30, 40]
print('Original List : ', orgList)
subList = [11,12,13]
orgList[2][2][2].append(subList)
print("After adding sublist : ",orgList)

# todo Exercise 9: Replace list’s item with new value if found
print('\nExercise 9: Replace list’s item with new value if found')
original_list=[5, 10, 15, 20, 25, 50, 20]
print("original list : ", original_list)
vl = original_list.index(20)
original_list[vl]=11
print("After removing 20 : ", original_list)
# todo Exercise 10: Remove all occurrences of a specific item from a list.
print('\nExercise 10: Remove all occurrences of a specific item from a list.')
original_list=[5, 10, 15, 20, 25, 50, 20]
print("original list : ", original_list)
while 20 in original_list:
    original_list.remove(20)
print("After removing multiple ocurance : ",original_list)

