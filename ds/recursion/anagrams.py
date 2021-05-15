# APPROACH
# (1) define a function called anagram
# (2) we run a loop 'n' times for each letter in the input string
# (3) in the beginning of the loop, we call the anagram() method for n-1 letters
# (4) after we return from this method, we perform a circular left-shift operation on the string and the loop continues...
# (5) BASE CONDITION: if only one letter is sent into the anagram() method then print the word

def circular_left_shift(string):
    first_chr = string[0]
    list_str = list(string)
    for i in range(0, len(list_str) - 1):          # loop should go till 2nd last character
        list_str[i] = list_str[i+1]
    list_str[-1] = first_chr

    return "".join(list_str)


def anagram(string, remains):
    new_string = string
    new_string_len = len(new_string)
    temp = remains
    if new_string_len == 1:
        print(remains+new_string)
        return

    for i in range(new_string_len):
        remains += new_string[0]
        anagram(new_string[1:], remains)
        remains = temp
        new_string = circular_left_shift(new_string)


anagram("ABC", "")
