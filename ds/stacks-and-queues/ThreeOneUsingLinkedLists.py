# Approach: Implementing a stack with sub-stacks using linked list
# Considering only for 3 stacks

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MultiStack:
    def __init__(self):
        self.num_of_stacks = 3
        self.top = [Node(None), Node(None), Node(None)]
        self.sizes = [0, 0, 0]
        self.top[0].next = self.top[1]
        self.top[1].next = self.top[2]
        self.top[2].next = None

    def is_empty(self, stack_id):
        return self.sizes[stack_id] == 0

    def push(self, stack_id, data):
        if self.is_empty(stack_id):
            self.top[stack_id].data = data
        else:
            temp = self.top[stack_id]
            self.top[stack_id] = Node(data)
            self.top[stack_id].next = temp
        self.sizes[stack_id] += 1

    def pop(self, stack_id):
        if self.is_empty(stack_id):
            print("Stack Underflow!")
        else:
            popped_element = self.top[stack_id].data
            self.top[stack_id] = self.top[stack_id].next
            self.sizes[stack_id] -= 1
            return popped_element


ms = MultiStack()
ms.push(0, 10)
ms.push(0, 20)
ms.push(1, 30)
ms.push(1, 40)
ms.push(2, 50)
ms.push(2, 60)
# Representation
# 20    ->      10      ->      40      ->      30      ->      60      ->      50      ->      None
# (TOP0)                        (TOP1)                          (TOP2)
print(ms.pop(0))
print(ms.pop(0))
print(ms.pop(1))
print(ms.pop(1))
print(ms.pop(2))
print(ms.pop(2))
