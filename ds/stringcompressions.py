def stringCompression(string):
    compressed_string = []
    counter = 0
    for i in range(len(string)):
        counter += 1
        if i == len(string) - 1 or string[i] != string[i + 1]:
            compressed_string.append(string[i])
            compressed_string.append(str(counter))
            counter = 0

    if len(compressed_string) >= len(string):
        return string
    return "".join(compressed_string)


print(stringCompression("abccccc"))
print(stringCompression("a"))

# NOTEWORTHY: In Approach 2,
# JAVA: String.valueOf(countConsecutive).length()
# Why?
# The number for digits required for writing a number in the compressed_string might vary.
# We might sometimes require 2 digit numbers. Hnece, we need to calculate the len(str(total_occurences_of_a_char))
# Because we cannot simply add +1 as the no. of digits may vary