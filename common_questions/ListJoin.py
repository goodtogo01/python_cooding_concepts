import collections

a = [4, 5, 6]
b = [1, 2, 3]

# Join list method 1
c = a + b
print("Method 1 : ", sorted(c))

# Join list method 2
for i in b:
    a.append(i)
print("method 2 : ", a)

# Join list method 3
m = [1,2,3,4,5]
n = [3,4,5,6,7]

m.extend(n)
print("Method 3 : ", sorted(m))

# Remove duplicates from the list
Method1 = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7,7,7]
Method2 = [1, 2, 3, 3, 4, 4]
def remD(m):
    # t = sorted(m)
    return list(set(m))

print("Remove duplicate : ", remD(Method1))

def mergNODup(a, b):
    t = set(a).union(set(b))
    return sorted(list(t))

print("remove dup and merge lists : ", mergNODup(Method1, Method2))

# common item from both list
x = [1,2,3,4,5]
y = [3,4,5,6,7]
def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

print(find_common_elements(x, y))

# Frequency of elements from the list
dup = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7,7,7]
d  = collections.Counter(dup)
print(dict(d))

s= "If you already have an older version of the Fliqlo screensaver installed"
g = collections.Counter(s)
print(dict(g))
