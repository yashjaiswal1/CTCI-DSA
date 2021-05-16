# Merge Sort implementation using 2-way merging
# Approach
# MergeSort(low, high)
# (1) calculate mid = (low+high)/2
# (2) if low < high then
#       (a) MergeSort(low, mid); MergeSort(mid+1, high); Merge(a, b)
#     return
# Merge(l1, l2)
# run a loop over l1
# compare elements from l1 and l2 at each step and append accordingly in new arr
# stop if anyone of the list finishes and append remaining elements of other list

def merge(list1, list2):
    """
    Prerequisite: list1 and list2 should be sorted.

    Returns a merged sorted array containing elements from list1 and list2.
    """
    result = []
    i = j = 0
    len_list1 = len(list1)
    len_list2 = len(list2)
    while(i < len_list1 and j < len_list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    for x in range(i, len_list1):
        result.append(list1[x])
    for x in range(j, len_list2):
        result.append(list2[x])
    return result


# the array can be provided as an additional third argument as per the requirement
# here, I personally didn't include it so as to reduce the internal memory stack size
def mergesort(low, high):
    """
    Returns the sorted array given the lowest and highest indices of the array.
    """

    # base caase occurs when low = high
    if low == high:
        return [arr[low]]

    else:
        mid = (low+high)//2
        l1 = mergesort(low, mid)
        l2 = mergesort(mid+1, high)
        return merge(l1, l2)


# custom test cases
# don't forget to change the low and high values when calling mergesort() method
# arr = [9, 6, 2, 3, 5, 1, 0]
# arr = [1, 0]
# arr = [-1]
# arr = [2, 1, 4, 0]
# arr = [2, 1, 4]
# arr = [1, 2, 3, 4]
arr = [4, 3, 2, 1, 0]
print(mergesort(0, 4))
