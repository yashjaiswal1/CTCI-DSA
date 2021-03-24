# Accept a string which may have black spaces
# Fill all the blank spaces between the characters with %20
# "Mr John Smith    " --> "Mr%20John%20Smith"
# True length (here, 13) is also given

# Approach 1

def urlify(string, true_len):
    input_list = list(string)
    space_count = 0
    # count the number of spaces
    for i in range(true_len):
        if(input_list[i] == ' '):
            space_count += 1
    index = true_len + space_count * 2
    for i in reversed(range(0, true_len)):
        if(input_list[i] == ' '):
            input_list[index - 1] = '%'
            input_list[index - 2] = '0'
            input_list[index - 3] = '2'
            index -= 3
        else:
            input_list[index - 1] = input_list[i]
            index -= 1
    print(''.join(input_list))


urlify('Mr John Smith    ', 13)
