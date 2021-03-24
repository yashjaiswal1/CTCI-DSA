# StringBuilder(arr_strings[])
# It is a function to concatenate multiple strings in a time efficient manner
# Conventionally, string concatenation would require a time complexity of O(x*(n)^2)
# x --> size of all strings, n --> no. of strings in arr_strings[] (or no. of strings to be concatenated)

def StringBuilder(arr_strings):
    print("".join(arr_strings))

StringBuilder(["aa","bb", "ajdahsjkd", "sajkdhajs", "xxx"])
