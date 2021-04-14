# Stack implementation using deque
# Deque stands for Double-Ended QUEue
# It is the optimal way to create stacks and queues in Python
# because it uses doubly-linked lists wherein, a new node is added as per the requirement
# whereas traditional python lists are dynamic and have to double their size (and copy those elements) when they hit their capacity

from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            print("Stack Underflow!")

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


some_numbers = Stack()
some_numbers.push(10)
some_numbers.push(20)
some_numbers.push(30)
print(some_numbers.size())
print(some_numbers.pop())
print(some_numbers.pop())
print(some_numbers.pop())
print(some_numbers.is_empty())
some_numbers.push(80)
some_numbers.push(90)

print(some_numbers.pop())
print(some_numbers.pop())
print(some_numbers.is_empty())
