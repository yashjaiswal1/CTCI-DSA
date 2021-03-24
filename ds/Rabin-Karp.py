# Rabin-Karp Algorithm
#ASSUMPTIONS:
# Main string (size = n) --> "abcdefghijklm"
# Substring (size = m) --> "jkl"
#
# It is a pattern matching algorithm used for finding substrings in a string
#   --> hash("abc") = code("a") * 127^2 + code("b") * 127^1 + code("c") * 127^0
#   --> Rolling Hash Method:
#       => hash("bcd") = (hash("abc") - code("a") * 127^2) * 127^1 + (code("d") * 127^0)
#       => check if hash of current substring matches with hash of required substring
#           => if hash is matching, check character-by-character if substring is same
#           => if hash not matching, skip to next substring
#       => This keeps repeating until we reach (n - m + 1)th element

from string import ascii_lowercase

def RKAlgo(mstr, pattern):
    code = {}
    flag = 1
    counter = 1
    for i in ascii_lowercase:
        code[i] = counter
        counter += 1
    substr = mstr[:3]
    substr_hash = code[mstr[0]] * 127 * 127 + code[mstr[1]] * 127 + code[mstr[2]]
    pattern_hash = code[pattern[0]] * 127 * 127 + code[pattern[1]] * 127 + code[pattern[2]]
    for i in range(len(mstr) - len(pattern) + 1):
        if(substr_hash == pattern_hash):
            for j in range(len(pattern)):
                if(substr[j] != pattern[j]):
                    flag = 0
                    break
            if(flag):
                print("Substring found at position: " + str(i))
                return
        if(i != (len(mstr) - len(pattern)) ):
            substr_hash = (substr_hash - code[mstr[i]] * 127 * 127) * 127 + code[mstr[i+3]]
            substr = mstr[i+1:i+4]
    print("Substring not found")


RKAlgo("abcdefghijklm", "abc")
RKAlgo("abcdefghijklm", "efg")
RKAlgo("abcdefghijklm", "klm")
RKAlgo("abcdefghijklm", "aaa")
RKAlgo("abcdefghijklm", "mmm")
