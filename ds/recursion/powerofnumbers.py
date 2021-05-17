# Approach to calculate power of any given number in (log n) time
# Simplified formula for calculating powers: (number)^power is equivalent to (number^2)^power/2 -- basically multiply and divide by 2 for the power
# Example: 2^8 is equal to (2^2)^8/2 = (2^2)^4
def power(x, y):
    if y == 1:
        return x
    else:
        result = power(x*x, y//2)
        if y % 2 == 1:
            result *= x
        return result


print(power(2, 1))
print(power(2, 2))
print(power(2, 3))
print(power(2, 4))
print(power(2, 5))
print(power(2, 6))
print(power(2, 7))
print(power(2, 8))
print(power(2, 9))
print(power(2, 10))
print(power(5, 7))
