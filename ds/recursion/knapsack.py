# APPROACH
# (1) pass the array of weights and target weight into the function
# (2) run a loop through all the items in the array
# (3) for each iteration, call the function recursively with updated target value and array as well
#       (a) new target value = old target value - currently selected weight
#       (b) new array should include all elements except the currently selected element
# (4) after loop runs out, return []
# STOP CASE: if at any moment, the target weight = 0 then stop


def knapsack(weights, target_weight):
    """
    Inputs: weights         ->  a list of weights
            target_weight   ->  an integer specifying the target weight (or knapsack capacity)

    Returns an array of weights whose sum is equal to the given target value
    """
    for i in weights:                                       # select a weight from the weights list one-by-one

        # creating a copy of weights list
        temp = weights[:]

        # remove the currently selected weight from the list because we want to exclude the currently selected weight
        # when we pass the weights list inside the recursive function
        temp.remove(i)

        # reduce the current target weight by subtracting it with the currently selected weight
        # we do this because we will be passing it into the recursive function
        new_target_weight = target_weight - i

        # if weight is still remaining
        if new_target_weight > 0:
            answer = knapsack(temp, new_target_weight)
            # answer will always be [] if nothing was found (or when we reach a condition wherein we exhaust all the elements in the weights list)
            if answer == []:
                continue
            # answer will have at least one element if we reached the target_weight = 0 condition
            else:
                return [i] + answer

        # if no weight is remaining (BASE CONDITION)
        elif new_target_weight == 0:
            return [i]

        # if our new_target_weight is -ve because, currently selected weight (i) > our current target_weight
        else:
            continue

    # if a knapsack method exhausts all the elements from the weights list then we should return back and try some other element
    # from the weight lists of outer recursive methods
    return []


print(knapsack([11, 8, 7, 6, 5], 20))
print(knapsack([11, 8, 7, 6, 5], 21))
print(knapsack([11, 8, 7, 6, 5], 22))
print(knapsack([11, 8, 7, 6, 5], 22))
