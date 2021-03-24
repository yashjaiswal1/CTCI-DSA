# Determine if a string has all unique characters
def is_unique(input_str):
    counter = {}

    if (len(input_str) > 128):
        return False

    for i in input_str:
        if(counter.get(i) == None):
            counter[i] = True
        else:
            return False
    return True

print(is_unique("abcdefghijk"))

# Alternatives
# (1)   Compare each and every character in the string. Time Complexity = O(n * n), Space Complexity = O(1)
# (2)   Sort the string in O(n logn) time and then search for neighbouring positions for repetitions
# These are not optimal solutions but can be used depending on the constraints of the problem.
