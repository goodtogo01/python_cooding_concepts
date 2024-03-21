# Exercise 1: Convert two lists into a dictionary
# Exercise 2: Merge two Python dictionaries into one
# Exercise 3: Print the value of key ‘history’ from the below dict
# Exercise 4: Initialize dictionary with default values
# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Exercise 6: Delete a list of keys from a dictionary
# Exercise 7: Check if a value exists in a dictionary
# Exercise 8: Rename key of a dictionary
# Exercise 9: Get the key of a minimum value from the following dictionary
# Exercise 10: Change value of a key in a nested dictionary


import json
# Exercise 1: Convert two lists into a dictionary
list1 = ['One', 'Two', 'Three']
list2 = [1,2,3]
converted_dict = dict(zip(list1, list2))
print("Convert two lists into a dictionary : ", converted_dict)
# Exercise 2: Merge two Python dictionaries into one
dic1 = {'One': 1, 'Two': 2, 'Three': 3}
dic2 = {'Three': 3, 'four': 4, 'Five': 5}
dic3 = {**dic1, **dic2}
print("\nMerged dictionaries with dict view: ", dict(dic3, indent=3))
print("\nMerged dictionaries with json view : ", json.dumps(dic3, indent=3))