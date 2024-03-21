
num = [2,3,45,1, 7,2,7]
print(num)

def big_and_small(number, n):
    number.sort()
    return number[-n:]

bigNUm = big_and_small(num, 1)
print("Sorted List : ", num)
print("big num : ", bigNUm)
print("small num : ", num[0])




def rev_int(i):
    num = i
    string = str(i)
    string = "".join(reversed(string))
    num = int(string)
    return num

print("rev int ", rev_int(321))