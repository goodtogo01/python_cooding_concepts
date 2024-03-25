# https://pynative.com/python-data-structure-exercise-for-beginners/
import collections
import json

# TODO Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the
#  second list

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
"""Using Slicing"""
odd_index_list1 = l1[1::2]
print("Odd index from list 1 : ", odd_index_list1)
even_index_list2 = l1[0::2]
print("Even index from list 2 : ", even_index_list2)
final_list = odd_index_list1 + even_index_list2
print("Final list : ", final_list)  # can use sorted, reversed

# TODO Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list

sample_list = [34, 54, 67, 89, 11, 43, 94]
print("\nOriginal list where elements are available : ", sample_list)

element = sample_list.pop(4)
print("List after removing element at index 4 : ", sample_list)
sample_list.insert(2, element)
print("List after adding element at index 2 : ", sample_list)
sample_list.append(element)
print("List after adding element at last : ", sample_list)
print()

# TODO Exercise 3: Slice list into 3 equal chunks and reverse each chunk
print("\nSlice list into 3 equal chunks and reverse each chunk: ")
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list : ", sample_list)
length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get index
    index = slice(start, end)

    # get chanks
    list_chunk = sample_list[index]
    print("chunk ", i, ":", list_chunk)

    # reverse chunk
    print("After reversring it : ", list(reversed(list_chunk)))

    start = end
    end += chunk_size

# TODO Exercise 4: Count the occurrence of each element from a list
print('\nExercise 4: Count the occurrence of each element from a list')
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
occurances = collections.Counter(sample_list)
print(dict(occurances), "\n")

# TODO Exercise 5: Create a Python set such that it shows the element from both lists in a pair
print('Exercise 5: Create a Python set such that it shows the element from both lists in a pair')
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
set_ele = set(zip(first_list, second_list))  # set, list, tuple, dict
print(set_ele)

# TODO Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set?
print('\nExercise 6: Find the intersection (common) of two sets and remove those elements from the first set?')

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print("----------------- Method 1:  ------------------------")
t = first_set.intersection(second_set)
print(f"Common elements between : ", t)
f = []
for i in first_set:
    if i not in t:
        f.append(i)

print(f"First Set is : {first_set}\nRemoved common elements are {t}, \nAnd rest of the elements are: ", set(f))

print("\n----------------- Method 2:  ------------------------")
intersections = first_set.intersection(second_set)
print("Common elements are : ", intersections)

for i in intersections:
    first_set.remove(i)  # remove common elements
print("First set after removing common elements : ", first_set)

# TODO Exercise 7: Checks if one set is a subset or superset of another set. If found,
#  delete all elements from that set
print("\nExercise 7: Checks if one set is a subset or superset of another set. If found,"
      "delete all elements from that set")
first_set = {57, 83, 29, 48}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First set is subset of Second_set: ", first_set.issubset(second_set))
print("Second_set is subset of First_set: ", second_set.issubset(first_set))

print("\nFirst set is Superset of Second_set: ", first_set.issuperset(second_set))
print("Second_set is superset of First_set: ", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("\nFirst Set : ", first_set)
print("Second Set : ", second_set)

print()
# todo Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not,
#   delete it from the list
print('\nExercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. '
      'If not, delete it from the list')

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print("Method 1: ")
removed_list = []
for i in sample_dict.values():
    if i in roll_number:
        removed_list.append(i)  # generate new list with dict - values
print("After removing unwanted items : ", removed_list)
print("\nMethod 2: ")
roll_number[:] = [i for i in roll_number if i in sample_dict.values()]
print("\nAfter removing unwanted items : ", roll_number)

# todo Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
print('\nExercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates')
speed = {'jan': 47, 'feb': 52, 'march': 47,
         'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54
         }
value_only = list(speed.values())
print("Only value from dictionary : ", value_only)


def no_dup(d):
    return sorted(set(d))

print("Fetch values and remove duplicate : ", no_dup(value_only))
# todo Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
print('\nExercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number')
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("Original List : ", sample_list)
unique_item = set(sample_list)
print("Only Unique Items : ", sorted(list(unique_item)))
tuple_item = tuple(unique_item)
print("Tuple items : ", tuple_item)
print("Max : ", max(tuple_item), "\nMin : ", min(tuple_item))

