# # todo Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
# print('\nExercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number')
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# noDup = set(sample_list)
# print("remov dup : ", noDup)
# mytup = tuple(noDup)
# print("convert into tuple : ", mytup)
# print("min : ", min(mytup), "\nmax : ", max(mytup))
nestedLoop = [10, 20, [300, 400, [5000, 6000, [199]], 500], 30, 40]
nestedLoop[2][2][2].append(9852)
print(nestedLoop[2][2][2][1])
