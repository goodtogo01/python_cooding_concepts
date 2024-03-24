# https://pynative.com/python-data-structure-exercise-for-beginners/
# TODO Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
import collections
import json

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
"""Using Slicing"""
odd_index_list1 = l1[1::2]
print("Odd index from list 1 : ", odd_index_list1)
even_index_list2 = l1[0::2]
print("Even index from list 2 : ", even_index_list2)
final_list = odd_index_list1+even_index_list2
print("Final list : ", final_list) # can use sorted, reversed

# TODO Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list

sample_list = [34, 54, 67, 89, 11, 43, 94]
print("\nOriginal list where elements are available : ", sample_list)

element= sample_list.pop(4)
print("List after removing element at index 4 : ", sample_list)
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list
sample_list.insert(2, element)
print("List after adding element at index 2 : ", sample_list)

sample_list.append(element)
print("List after adding element at last : ", sample_list)
print()
# TODO Exercise 3: Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list : ", sample_list)
length = len(sample_list)
chunk_size = int(length/3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get index
    index = sample_list[0::3] # slice(start, end)

    # get chanks
    list_chunk = sample_list[index]
    print("chunk ", i, list_chunk)

    # reverse chunk
    print("After reversring it : ", list(reversed(list_chunk)))

    start = end
    end += chunk_size



# Exercise 4: Count the occurrence of each element from a list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
occurances = collections.Counter(sample_list)
print(dict(occurances))


# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
f = dict(zip(first_list, second_list))

print(json.dumps(f, indent=4))
# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set?
# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not,
#   delete it from the list
# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates

# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number