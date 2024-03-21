#Lambda functions are also called anonymous functions. An anonymous function is a function defined without a name


# solution with reguler function
def non_lambda(a, b):
    c = a+b
    return c
print(f"Non Lambda : ", non_lambda(10, 20))

# solution with lambda function where no name of function is required
with_lambda = lambda a, b : a+b
print("with lambda : ",with_lambda(10,20))