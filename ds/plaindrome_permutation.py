# (1) form a hash table and mark the number of occurences for each character in the string
# (2) if len(string) --> odd, all character counts should be even with only one odd character count
# (3) if len(string) --> even, all character counts should be even.
# (4) In conclusion, our final condition can be that there should be at most one odd character count


def isPermutationOfPalindrome(string):
    counter = 0
    count = {}
    string = string.upper().replace(" ", "")
    for i in string:
        if count.get(i) == None:
            count[i] = 1
        else:
            count[i] += 1
    return checkMaxOneOdd(count)


def checkMaxOneOdd(table):
    foundOdd = False
    for i in table:
        if table[i] % 2 == 1:
            if foundOdd:
                return False
            foundOdd = True
    return True


print(isPermutationOfPalindrome("atco cta"))

# Third implementation is not clear!