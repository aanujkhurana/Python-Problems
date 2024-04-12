# Recursive Function

# FACTORIAL SEQUENCE 
# factorial(n) = n * factorial(n-1)
def factorial(x):
    if (x == 0 or x == 1):
        return 1
    else:
        x = x * factorial(x-1)
        return x

f = factorial(1)
print(f)

# FIBONACCI SEQUENCE
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

p = fibonacci(32)
print(p)