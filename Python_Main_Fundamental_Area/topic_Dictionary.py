"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Duplicates Not Allowed
Dictionaries cannot have two items with the same key:

"""
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
# TODO Exercise 1: Convert two lists into a dictionary
list1 = ['One', 'Two', 'Three']
list2 = [1,2,3]
converted_dict = dict(zip(list1, list2))
print("Convert two lists into a dictionary : ", converted_dict)
# TODO Exercise 2: Merge two Python dictionaries into one
dic1 = {'One': 1, 'Two': 2, 'Three': 3}
dic2 = {'Three': 3, 'four': 4, 'Five': 5}
dic3 = {**dic1, **dic2}
print("\nMerged dictionaries with dict view: ", dict(dic3, indent=3))
print("\nMerged dictionaries with json view : ", json.dumps(dic3, indent=3))

# TODO Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
value_history = sampleDict['class']['student']['marks']['history']
print("\nPrint the value of key ‘history’ from the below dict : ",value_history)

# TODO Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
results = dict.fromkeys(employees, defaults)
print("\nInitialize dictionary with default values : ", json.dumps(results, indent=4))

# TODO  Exercise 5: Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
print("\nMethod 01 : using Update() functions")
res = dict()
for k in keys:
    res.update({k: sample_dict[k]})
print(res)

print("\nMethod 02 : using Loop comprehension")
res2 = {k: sample_dict[k] for k in keys}
print(res2)

# TODO Exercise 6: Delete a list of keys from a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york" # change city to location
}
print("\nActual dictionary : ", sample_dict)
forDel = ['salary', 'city']
for k in forDel:
    sample_dict.pop(k)
print(f"After deleting of {forDel} : ", sample_dict)
print()

# TODO Exercise 7: Check if a value exists in a dictionary
exist_value = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
if 25 in exist_value.values():
    print("Value of 25 is exist")
else:
    print("Value doesnt exist")
# TODO Exercise 8: Rename key of a dictionary
print()
rename_key = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
print("actual dictionary : ", rename_key)
rename_key['location']= rename_key.pop('city')
print("With new key after rename : ", rename_key)
print()

# TODO Exercise 9: Get the key of a minimum value from the following dictionary
minimum_key = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
min_value = min(minimum_key)
print("The key that belong minimum value : [", min_value, "] "
    "and holding value is : [", min(minimum_key.values()),"]")
print()
# TODO Exercise 10: Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
print("original dict : ", format(sample_dict))
sample_dict['emp3']['salary']=1212
print("After updating value of salary is : ", sample_dict)