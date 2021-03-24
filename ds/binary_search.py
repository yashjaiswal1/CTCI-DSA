def binary_search(arr, first, last, key):
	mid = (first + last) // 2
	if (first <= last):
		if(arr[mid] == key):
			print("Element found at index: " + str(mid))
			return
		elif(key > arr[mid]):
			return binary_search(arr, mid+1, last, key)
		elif(key < arr[mid]):
			return binary_search(arr, first, mid-1, key)
	return -1

def bsearch_insert(arr, first, last, val):
	mid = (first + last) // 2
	if (first <= last):
		if(arr[mid] == val):
			print("Element found at index: " + str(mid))
			return
		elif(val > arr[mid]):
			return binary_search(arr, mid+1, last, val)
		elif(val < arr[mid]):
			return binary_search(arr, first, mid-1, val)
	
	arr.append(0)
	for i in range(mid+1, len(arr), -1):
		arr[i] = arr[i+1]
	arr[mid+1] = val


arr = [1,2,3,5,10,11]
binary_search(arr,0,3,1)
binary_search(arr,0,3,2)
binary_search(arr,0,3,3)
binary_search(arr,0,3,5)
print(binary_search(arr,0,3,9))
bsearch_insert(arr, 0, 3, 7)