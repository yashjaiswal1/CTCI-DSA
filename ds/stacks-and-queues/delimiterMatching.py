# Matching each opening bracket ( or { or [ with it's closing bracket ] or } or ) order-wise
# Approach
# (1) accept a string consisting of alphanumeric characters which may have brackets in it
# (2) push every open bracket into a stack
# (3) if we come across a closing bracket then pop the stack and see if it matches with the popped bracket
# (4) if it does, then we move on
# (5) if not, then we stop and return false

def isBracketBalanced(input_string):
    stack = []
    for i in input_string:
        open_bracket_found = (i == '(' or i == '[' or i == '{')
        closed_bracket_found = (i == ')' or i == ']' or i == '}')
        if (open_bracket_found):
            stack.append(i)
        elif (closed_bracket_found):
            try:
                last_open_bracket = stack.pop()
            except IndexError:
                return False
            if((last_open_bracket == '(' and i == ')') or (last_open_bracket == '{' and i == '}') or (last_open_bracket == '[' and i == ']')):
                pass
            else:
                return False
    if(stack == []):
        return True
    else:
        return False


print(isBracketBalanced("[{()}]"))
