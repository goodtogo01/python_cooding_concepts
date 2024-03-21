a = [-1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
b = [-1, 4]
t = [2,3,4,5,-1,7]


def findMis(n):
    numbers = set(n)
    length = len(n)
    outPut = []

    for i in range(0, n[-1]):
        if i not in numbers:
            outPut.append(i)
    return outPut


# print("method 1 : ", end="")
# print(findMis(b))


def findMis2(k):
    res = []
    for i in range(min(k), max(k)):
        if i not in k:
            res.append(i)
    return res


# print("\nmethod 2 : ", end="")
# print(findMis2(b))


def ff(k):
    r = []
    for i in range(min(k), max(k)):
        if i not in k:
            r.append(i)
    return r


print("\nNo method : ", ff(b))
