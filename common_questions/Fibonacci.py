

def f(n):

    x = 0
    y = 1

    for i in range( 0, n):
        print(x, end=" ")
        z = x + y
        x = y
        y = z



# Fibonacci with user input
def fibonacci():
    n = int(input("Enter number  : "))
    a = 0
    b = 1

    for i in range(0 , n):
        print(a, end=" ")
        fibo = a + b
        a = b
        b = fibo


fibonacci()

