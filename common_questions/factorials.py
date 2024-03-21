import math


# Factorial without recursion
def factorials_01(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i

    print(f"Factorial for {n} without recurssion: ", fact)


# Factorial with recurssion
def factorial_02(n):

    if(n==0):
        return 1
    return n * factorial_02(n-1)


def factorial_03(n):
    print("Factorial with Math function: ", end="")
    print(math.factorial(n))


factorials_01(5)
print("Factorial with recurssion : ",factorial_02(5))
factorial_03(5)



