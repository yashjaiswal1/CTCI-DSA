# (1) Check length to determine what operation is to be performed.
#       (a) If |len(s1) - len(s2)| > 1, return False
#       (b) If |len(s1) - len(s2)| = 1, redirect to OneInsertAway() [same logic for deletion]
#       (c) If |len(s1) - len(s2)| = 0, redirect to OneReplaceAway()
# "CAT" and "COS"
# flag = True
# if flag already set to True, return False


def OneEditAway(string1, string2):
    if len(string1) + 1 == len(string2):
        return OneInsertAway(
            string1, string2
        )  # first param: shorter string, second param: longer string
    elif len(string1) == len(string2) + 1:
        return OneInsertAway(string2, string1)
    elif len(string1) == len(string2):
        return OneReplaceAway(string1, string2)
    else:
        return False


def OneInsertAway(s1, s2):
    index1 = 0  # index for string 1
    index2 = 0  # index for string 2
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] == s2[index2]:
            index1 += 1
            index2 += 1
        elif s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
    return True


def OneReplaceAway(s1, s2):
    index1 = 0
    index2 = 0
    flag = False
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if flag:
                return False  # indicating that more than 1 replace operations have been performed
            flag = True
        index1 += 1
        index2 += 1
    return True


print(OneEditAway("", "a"))