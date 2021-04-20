def IncreasingSubstring(n, string):
    string_length = len(string)
    current_substring = ""
    substring_positional_lengths = []
    for i in range(string_length):
        current_substring += string[i]
        substring_positional_lengths.append(str(len(current_substring)))

        if i == string_length - 1:
            return substring_positional_lengths
        elif string[i] < string[i+1]:
            pass
        else:
            current_substring = ""


t = int(input())
# n = []
# strings = []
# for _ in T:
#     n.append(int(input()))
#     strings.append(input())
for testnumber in range(1, t+1):
    n = int(input())
    string = input()
    output = IncreasingSubstring(n, string)
    print("Case #" + str(testnumber) + ": " + " ".join(output))
