# Robert Lafore - triangle numbers (iterative approach)
def triangle(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


print(triangle(4))
