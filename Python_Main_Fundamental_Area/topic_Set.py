"""
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
Note: Sets are unordered, so you cannot be sure in which order the items will appear.

Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.
"""

# todo Exercise 1: Add a list of elements to a set
print('Exercise 1: Add a list of elements to a set')
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
for i in sample_list:
    sample_set.add(i)
print(sample_set)

# todo Exercise 2: Return a new set of identical (Common Item) items from two sets
print('\nExercise 2: Return a new set of identical (Common Item) items from two sets')
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print(set3)
# todo Exercise 3: Get Only unique items and remove duplicates from two sets
print('\nExercise 3: Get Only unique items and remove duplicates from two sets')
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.union(set2)
print(set3)

# todo Exercise 4: Update the first set with items that don’t exist in the second set
print('\nExercise 4: Update the first set with items that don’t exist in the second set')
# difference_update() is used to update when same item not exist in another set
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)

# todo Exercise 5: Remove items from the set at once
print('\nExercise 5: Remove items from the set at once')
# following: Write a Python program to remove items 10, 20, 30 from the following set at once.
s ={10, 20, 30}
set1 = {10, 20, 30, 40, 50}
set1.difference_update(s)
print(set1)
# todo Exercise 6: Return a set of elements present in Set A or B, but not both
print('\nExercise 6: Return a set of elements present in Set A or B, but not both')
# symmetric_difference() return not common item from both set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
m = set1.symmetric_difference(set2)
print(m)

# todo Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
print('\nExercise 7: Check if two sets have any elements in common. If yes, display the common elements')
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
s = set1.intersection(set2)
print(s)

# todo Exercise 8: Update set1 by adding items from set2, except common items
print('\nExercise 8: Update set1 by adding items from set2, except common items')
# symmetric_difference() return not common item from both set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
s = set1.symmetric_difference(set2)
print(s)

# todo Exercise 9: Remove items from set1 that are not common to both set1 and set2
print('\nExercise 9: Remove items from set1 that are not common to both set1 and set2')
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
m = set1.intersection(set2)
print(m)


print('\n')
s1 = {1,2,3,4,5,8}
s2 = {4,5,6,7,8}
print(s1.union(s2), " union() --  is no dplicate")
print(s1.intersection(s2), " intersection() -- Only duplicate")
