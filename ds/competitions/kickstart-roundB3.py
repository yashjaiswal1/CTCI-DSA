import math


def isPrimeNumber(num):
    if num == 2:
        return True
    if ((num % 2 == 0) or (num < 2)):
        return False
    else:
        i = 3
        while(num >= (i ** 2)):
            if num % i == 0:
                return False
            i += 2
        return True


def ConsecutivePrimes(z):
    approximation = int(math.sqrt(z))
    primes = []
    max = -1
    for i in range(approximation - 50, approximation + 50):
        if i > 1 and isPrimeNumber(i):
            primes.append(i)

    for i in range(len(primes) - 1):
        current_product = primes[i] * primes[i+1]

        if current_product > max and current_product <= z:
            max = current_product
    return max


t = int(input())
for testnumber in range(1, t+1):
    z = int(input())
    output = ConsecutivePrimes(z)
    print("Case #" + str(testnumber) + ": " + str(output))
