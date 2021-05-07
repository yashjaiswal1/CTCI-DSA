# Robert Lafore - triangle numbers (iterative approach)
def triangle(n):
    if n == 0:
        return 0
    elif n < 0:
        raise ValueError("Triangle numbers cannot be a negative value")
    return n + triangle(n-1)


print(triangle(4))
# print(triangle(-1))       raises ValueError
