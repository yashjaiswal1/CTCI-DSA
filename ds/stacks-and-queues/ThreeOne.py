# Approach: Divide the stack into sub-stacks of fixed sizes
# top --> offset + current_size
# offset --> stack_number * capacity
# indexOf(0 || 1 || 2 || ...) --> top index of that particular stack number
# [10, 20, 30, 40, 50]
class MultiStack:

    def __init__(self, num_of_stacks, capacity):
        self.capacity = capacity            # expected input type: array
        self.current_size = [0] * num_of_stacks
        self.num_of_stacks = num_of_stacks
        self.stack = []
        for i in self.capacity:
            self.stack += [None] * i

    def index_of(self, stack_id):
        i = offset = 0
        while i != stack_id:
            offset += self.capacity[i]
            i += 1
        return (offset + self.current_size[stack_id] - 1)

    def is_empty(self, stack_id):
        return self.current_size[stack_id] == 0

    def push(self, stack_id, data):
        if self.current_size[stack_id] == self.capacity[stack_id]:
            print("Stack Overflow!")
        else:
            self.current_size[stack_id] += 1
            self.stack[self.index_of(stack_id)] = data

    def pop(self, stack_id):
        if self.current_size[stack_id] == 0:
            print("Stack Underflow!")
        else:
            temp = self.stack[self.index_of(stack_id)]
            self.stack[self.index_of(stack_id)] = None
            self.current_size[stack_id] -= 1
            return temp

    def printStack(self):
        print(self.stack)


ms = MultiStack(3, [3, 3, 3])
ms.printStack()
ms.push(stack_id=1, data=30)
ms.push(stack_id=0, data=10)
ms.push(stack_id=2, data=50)
ms.push(stack_id=0, data=20)
ms.push(stack_id=2, data=60)
ms.push(stack_id=1, data=40)
ms.push(stack_id=0, data=70)
ms.push(stack_id=0, data=80)
print(ms.pop(0))
print(ms.pop(1))
print(ms.pop(2))
print(ms.pop(2))
print(ms.pop(2))
ms.printStack()
