def numbers(a, b):
    if (a > b):
        print("a is Greater then b")
    else:
        print(" b is Greater then a")


numbers(6,65)

def big_and_small_number(number, n):
    number.sort()
    return number[-n: ]

num = [1,4,3,2,5,6,7,6,54,3]
print("Original List is ", num)
sortedLists = big_and_small_number(num, 1)
print("Sorted list : ", num)
print("Bigest number from the list is : ", sortedLists)
print("Smallest number from the list is : ", num[0])