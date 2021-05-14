# Recursive approach
# (1) input an array of sorted integers and the key to be found
# (2) calculate mid = (low+high)/2
# (3) if key > mid then return bsearch(mid+1, high, key)
# (4) if key < mid then return bsearch(low, mid-1, key)
# (5) if key == mid then return index
# (6) if high < low then return False

def bsearch(low, high, key):
    mid = (low + high)//2
    if low > high:
        return False
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return bsearch(mid+1, high, key)
    if key < arr[mid]:
        return bsearch(low, mid-1, key)


arr = [1, 2, 3, 4, 5, 6, 7]
print(bsearch(0, 6, 1))
print(bsearch(0, 6, 2))
print(bsearch(0, 6, 3))
print(bsearch(0, 6, 4))
print(bsearch(0, 6, 5))
print(bsearch(0, 6, 6))
print(bsearch(0, 6, 7))
print(bsearch(0, 6, -10))
print(bsearch(0, 6, 100))
