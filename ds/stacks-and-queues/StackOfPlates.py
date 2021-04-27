from collections import deque
from typing import Deque


class SetOfStacks:

    def __init__(self, capacity):
        self.set_of_stacks = []
        self.capacity = capacity

    def getLastStack(self):
        return self.set_of_stacks[-1] if self.set_of_stacks != [] else Deque()

    def push(self, data):
        current_stack = self.getLastStack()
        is_stack_full = len(current_stack) == self.capacity
        if (self.set_of_stacks != [] and is_stack_full != True):
            current_stack.append(data)
        else:
            current_stack = Deque()
            self.set_of_stacks.append(current_stack)
            current_stack = self.getLastStack()  # remove this line
            current_stack.append(data)

    def pop(self):
        current_stack = self.getLastStack()

        if (self.set_of_stacks == []):
            print("Stack Underflow!")
            return
        popped_element = current_stack.pop()

        is_stack_empty = len(current_stack) == 0
        if is_stack_empty:
            self.set_of_stacks.pop()

        return popped_element


StackOfPlates = SetOfStacks(3)
StackOfPlates.pop()
print(StackOfPlates.set_of_stacks)
StackOfPlates.push(10)
print(StackOfPlates.set_of_stacks)
StackOfPlates.push(20)
print(StackOfPlates.set_of_stacks)
StackOfPlates.push(30)
print(StackOfPlates.set_of_stacks)
StackOfPlates.push(40)
print(StackOfPlates.set_of_stacks)
StackOfPlates.push(50)
print(StackOfPlates.set_of_stacks)
StackOfPlates.push(60)
print(StackOfPlates.set_of_stacks)
StackOfPlates.push(70)
print(StackOfPlates.set_of_stacks)
StackOfPlates.pop()
print(StackOfPlates.set_of_stacks)
StackOfPlates.pop()
print(StackOfPlates.set_of_stacks)
StackOfPlates.pop()
print(StackOfPlates.set_of_stacks)
StackOfPlates.pop()
print(StackOfPlates.set_of_stacks)
StackOfPlates.pop()
print(StackOfPlates.set_of_stacks)
StackOfPlates.pop()
print(StackOfPlates.set_of_stacks)
StackOfPlates.pop()
print(StackOfPlates.set_of_stacks)
StackOfPlates.pop()
