# Approach:
# Every node should have a local minimum and there will be a global minimum
# the local minimum of new_node will accept minimum(new_node.data, global_minimum)
# Thus, we will have a minimum value associated with each state of the stack

class Node:
    def __init__(self, data):
        self.data = data
        self.minimum = None
        self.next = None


class Stack:
    # latest top minimum acts as global minimum
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, data):
        if self.is_empty():
            self.top = Node(data)
            self.top.minimum = self.top.data
        else:
            # transform current top into new_node
            # set new_node.next as current top
            new_node = Node(data)
            new_node.minimum = new_node.data if new_node.data < self.top.minimum else self.top.minimum
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
        else:
            popped_element = self.top.data
            self.top = self.top.next
            return popped_element

    def get_minimum(self):
        return self.top.minimum if self.top != None else None


stack_instance = Stack()
stack_instance.push(30)
stack_instance.push(20)
stack_instance.push(10)
print("Minimum = ", stack_instance.get_minimum())
print(stack_instance.pop())
print("Minimum = ", stack_instance.get_minimum())
print(stack_instance.pop())
print("Minimum = ", stack_instance.get_minimum())
print(stack_instance.pop())
print("Minimum = ", stack_instance.get_minimum())
