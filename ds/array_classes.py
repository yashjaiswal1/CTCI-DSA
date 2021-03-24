class ArrayApp:
	def __init__(self):
		self.arr = []
		self.num = 0

	def insert_arr(self, value):
		self.arr.append(value)
		self.num += 1

	def search_arr(self, key):
		for x in range(self.num):
			if key == self.arr[x]:
				return x
		print("Key not found")

	def delete_arr(self, value):
		for x in range(self.num):
			if value == self.arr[x]:
				break
		if self.arr[x] != value:
			print("Valuez not found")
			return
		print("works")
		for i in range(x, self.num - 1):
			self.arr[i] = self.arr[i+1]
		self.num -= 1
	
	def print_arr(self):
		print(self.arr)
		print(self.num)

arr1 = ArrayApp()
arr1.insert_arr(10)
arr1.insert_arr(20)
arr1.insert_arr(30)
arr1.print_arr()
print(arr1.search_arr(30))
arr1.delete_arr(20)
arr1.print_arr()
arr1.search_arr(20)
arr1.delete_arr(40)
