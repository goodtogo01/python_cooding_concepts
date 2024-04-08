"""
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.

Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:
"""
import collections
# todo Exercise 1: Reverse the tuple

print('Exercise 1: Reverse the tuple')
tuple1 = (10, 20, 30, 40, 50)
print('Original Tuple : ', tuple1)
f = tuple1[::-1]
print("After Reversed : ", f)
# todo Exercise 2: Access value 20 from the tuple
print('\nExercise 2: Access value 20 from the tuple')
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print('Original Tuple : ', tuple1)
acc = tuple1[1][1]
print(f"Access at desire value of : ", acc)

# todo Exercise 3: Create a tuple with single item 50
print('\nExercise 3: Create a tuple with single item 50')
create_tuple = (50, )
print("Single item as : ", create_tuple)

# todo Exercise 4: Unpack the tuple into 4 variables
print('\nExercise 4: Unpack the tuple into 4 variables')
tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
for i in tuple1:
    print(a)
    print(b)
    print(c)
    print(d)
    break
# todo Exercise 5: Swap two tuples in Python
print('\nExercise 5: Swap two tuples in Python')
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)



# todo Exercise 6: Copy specific elements from one tuple to a new tuple
print('\nExercise 6: Copy specific elements from one tuple to a new tuple')
tuple1 = (11, 22, 33, 44, 55, 66)
ll=tuple1[3:-1]
print(ll)


# todo Exercise 7: Modify the tuple
print('\nExercise 7: Modify the tuple')
#  modify 22 as 222
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)
# todo Exercise 8: Sort a tuple of tuples by 2nd item
print('\nExercise 8: Sort a tuple of tuples by 2nd item')
tuple1 = (('l', 31),('a', 23),('b', 37),('c', 11), ('d',29))
tuple1 = tuple(sorted(set(tuple1), key= lambda x:x[1]))
print(tuple1)
# todo Exercise 9: Counts the number of occurrences of item 50 from a tuple
print('\nExercise 9: Counts the number of occurrences of item 50 from a tuple')
tuple1 = (50, 10, 60, 70, 50)
tup1=tuple1.count(50)
print("50 is occurance at '",tup1,"' times")
# todo Exercise 10: Check if all items in the tuple are the same
print('\nExercise 10: Check if all items in the tuple are the same')
t1 = (45, 45, 45, 45,)
m = all(i == t1[0] for i in t1)
print(m)

