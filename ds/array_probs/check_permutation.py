# Given 2 strings, check if they are permutations of each other

# Approach 1: with Hash
# hash(str1) = hash(str2)

# def check_permutation(str1, str2):
#     if(hash(str1) == hash(str2)):
#         return True
#     return False
# print(check_permutation('abcdef', 'abcdef'))


# Approach 2: with Dict (most efficient)
# counter = {'a':1, 'b':2, ...} do this for str1
# iterate through string 2 and check for the characters in counter:
#   (i)     if character doesn't exist in counter, then return False
#   (ii)    if character exists, decrement it's value by 1

# def check_permutation(str1, str2):
#     counter = {}
#     if (len(str1) != len(str2)):
#         return False

#     for c in str1:
#         if counter.get(c) == None:  # if counter doesn't have the element 'c' then initialize by 1
#             counter[c] = 1
#         else:
#             counter[c] += 1         # else, increment by 1

#     for c in str2:
#         # element should exist AND element's value shouldn't be 0
#         if(counter.get(c) != None and counter[c] != 0):
#             counter[c] -= 1
#         else:
#             return False
#     return True


# print(check_permutation("abcd", "dacb"))

# Approach 3: sort both strings and then compare both of them (most simple to explain but not efficient)
def check_permutation(str1, str2):
    if(len(str1) != len(str2)):
        return False
    l1 = list(str1)
    l2 = list(str2)
    l1.sort()
    l2.sort()
    if(l1 == l2):
        return True
    else:
        return False


print(check_permutation("abc", "bac"))
