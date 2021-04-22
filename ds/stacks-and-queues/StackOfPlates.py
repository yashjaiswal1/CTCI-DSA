from collections import deque


class SetOfStacks:

    def __init__(self, capacity):
        self.set_of_stacks = []
        self.capacity = capacity
        self.current_stack = None
        self.current_stack_size = 0

    def push(self, data):
        if (self.current_stack_size == 0):
            self.current_stack = deque()
            self.set_of_stacks.append(self.current_stack)
        elif (self.current_stack_size == self.capacity):
            # generate a new stack
        self.current_stack.append(data)
