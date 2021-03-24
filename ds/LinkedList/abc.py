# Approach
# (1) Accept input of number of test cases in a single variable
# (2) Accept a string in a temp var and assign the N and K values from that string into respective arrays (n[], k[]) using slicing
# (3) Accept the string S for every testcase and store it in it's respective array s[]
# (4) Check the goodness score of given string; define 1<=i<=n/2
# (5) If score is equal to given K then return 0
# (6) If score > k then:
#       (a) find a pair of goodstring number which are unequal
#       (b) replace the right number with the same number as the left number
#       (c) repeat until score = k
# (7) If score < k then:
#       (a) find a pair of goodstring number which are equal
#       (b) replace the right number with another number such that the pair becomes unequal
#       (c) repeat until score = k
# Repeat for all test cases

def GetGoodnessScore(s, n):
    score = 0
    for i in range(1, int(n/2)+1):
        if (s[i - 1] != s[n-i+1 - 1]):
            score += 1
    return score


test_cases = int(input())
s = []
k = []
n = []
answers = []
for inp in range(test_cases):
    temp = input()
    n.append(int(temp[0]))
    k.append(int(temp[2]))
    s.append(input())

for iteration in range(test_cases):
    current_score = GetGoodnessScore(s[iteration], n[iteration])
    if(current_score == k[iteration]):
        answers.append(0)
    else:
        answers.append(abs(current_score - k[iteration]))
