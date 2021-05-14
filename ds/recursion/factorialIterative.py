def factorial(n):
    result = 1

    # error handling
    if n < 0:
        raise ValueError(
            "Factorial can be computed strictly for positive integers.")
    if n - int(n) > 0:
        raise TypeError(
            "Factorial cannot be computed for floating-point numbers.")
    # iterative logic
    while n != 0:
        result = result * n
        n -= 1
    return result


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(5))
print(factorial(10))
# print(factorial(1.5))     raises TypeError
# print(factorial(-1))      raises ValueError
