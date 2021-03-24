# compute hassh of pattern
# compute hash of first 3 chars of mstring
# compare hash:
#   if hash matches, compare the two strings
#   if hash doesn't match, skip to next string
# initial hash('abc') = code('a') * 127^2 + code('b') * 127 + code('c')
# Rolling hash(for successive characters): hash('bcd') = ( hash('abc') - code('a')*127^2 ) * 127 + code('d')
# no. of iterations required = len(mstring) - len(pattern) + 1
# 5 - 3 = 2 (n-1) ==> 2+1 = 3
from string import ascii_lowercase

def RKAlgo(mstring, pattern):
    code = {}
    counter = 1
    for i in ascii_lowercase:
        code[i] = counter
        counter += 1
    hash_pattern = code[pattern[0]] * 127 * 127 + code[pattern[1]] * 127 + code[pattern[2]]
    hash_current = code[mstring[0]] * 127 * 127 + code[mstring[1]] * 127 + code[mstring[2]]
    for i in range(len(mstring) - len(pattern) + 1):
        if(hash_current == hash_pattern and mstring[i: i+3] == pattern[0:3]):
            print("Pattern found at position: " + str(i))
            return
        if(i != len(mstring) - len(pattern) ):
            hash_current = ( hash_current - code[mstring[i]] * 127 * 127 ) * 127 + code[mstring[i+3]]
    print("Pattern not found")

RKAlgo("abcdefghijkl", "def")
