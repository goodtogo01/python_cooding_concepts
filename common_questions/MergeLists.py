# Merg list
a = [1, 2, 3, 4, 5, 5, 1, 0, 1, 9]
b = [5, 6, 7, 8, 9]
c = a + b
print(c)


# sort and merge lists and skip duplicate
def sm(a, b):
    p = set(a).union(set(b))
    return sorted(list(p))


print("Merge two lists and skip duplicate values: ", sm(a,b))

# Skip duplicate from a list
def ls(l):
    p = sorted(set(l))
    return p

print("Merg List and skip duplicate values : ", ls(a))