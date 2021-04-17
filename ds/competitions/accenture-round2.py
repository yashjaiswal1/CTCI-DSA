def sensor1(L, R):
    result = [None, 1]
    repetitions = 1
    for i in range(1, R+1):
        repetitions = 2**(i - 1)
        while(repetitions):
            if len(result) == R+1:
                break
            result.append(2**i)
            repetitions -= 1
    return result[L:R+1]


def sensor2(L, R, X):
    result = []
    for i in range(1, R+1):
        for j in range(X):
            if len(result) == R:
                break
            result.append(X*i)
    return result[L-1:]


def solve(L, R, X):
    arr1 = sensor1(L, R)
    arr2 = sensor2(L, R, X)
    sensor1_early_count = 0
    sensor2_early_count = 0
    for i in range(R - L + 1):
        if arr1[i] < arr2[i]:
            sensor1_early_count += 1
        elif arr2[i] < arr1[i]:
            sensor2_early_count += 1

    if sensor1_early_count > sensor2_early_count:
        return 1
    elif sensor2_early_count > sensor1_early_count:
        return 2
    else:
        return 0


print(sensor2(5, 10, 2))
T = int(input())
for _ in range(T):
    L, R, X = map(int, input().split())
    out_ = solve(L, R, X)
    print(out_)
