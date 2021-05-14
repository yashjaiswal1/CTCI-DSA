def factorial(n):

    # base case
    if n == 0:
        return 1

    # error handling
    if n < 0:
        raise ValueError(
            "Factorial can be computed strictly for positive integers.")
    if n - int(n) > 0:
        raise TypeError(
            "Factorial cannot be computed for floating-point numbers.")

    # recursive logic
    return n * factorial(n-1)


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(5))
print(factorial(10))
# print(factorial(1.5))     raises TypeError
# print(factorial(-1))      raises ValueError
