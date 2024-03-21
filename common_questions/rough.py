a = [1, 4, 7, 9, 0, -9, 8, 7, 676]
b = [3, 2, 1, 7, 8, 1, 0, 2]


# sort list and remove duplicate
def ss(n):
    p = sorted(set(n))
    return p


print("sorted list and skiped duplicates : ", ss(a))


# merge lists with remove duplicates
def kk(m, n):
    p = set(m).union(set(n))
    return sorted(list(p))


print("\nMerge list with no duplicates : ", kk(a, b))


# fibonacci series with user input

def ff():
    n = int(input("Enter your numnber : "))
    a = 0
    b = 1
    for i in range(0, n):
        print(a, end=" ")
        fibo = a + b

        a = b
        b = fibo


# ff()

s = [0, 3, 3, 3, 4, 5, 9]
t = [1, 2, 3, 4, 5, 5, 5]


def mis(m):
    res = []
    for i in range(min(m), max(m)):
        if i not in m:
            res.append(i)
    return res


def dup(a, b):
    h = set(a).union(set(b))
    return sorted(list(h))


print("sorted list : ", dup(s, t))

print("Missisn number is : ", mis(s))
