def CheckPossibleNumberExists(left, right, current_difference):
    new_element = left - current_difference
    if ((left - new_element) == (new_element - right)):
        return True
    return False


def GetLongestProgression(n, sequence):
    differences = []
    for i in range(n - 1):
        differences.append(sequence[i] - sequence[i+1])

    current_difference = differences[0]
    max = n
    counter = 0
    print(differences)
    for i in range(len(differences)):
        try:
            if differences[i] == current_difference:
                counter += 1
            elif((differences[i] != current_difference) and (i + 1 + 1 != n - 1) and (CheckPossibleNumberExists(sequence[i + 1 - 1], sequence[i + 1 + 1], current_difference))):
                secondary_index = i + 1
                while(differences[secondary_index] == current_difference):
                    counter += 1
                    secondary_index += 1
                if max < counter + 1:
                    max = counter + 1
                counter = 1
                current_difference = differences[i]
        except IndexError:
            pass
    return max


t = int(input())
for testnumber in range(1, t+1):
    n = int(input())
    sequence = map(int, input().split())
    output = GetLongestProgression(n, list(sequence))
    print("Case #" + str(testnumber) + ": " + str(output))
