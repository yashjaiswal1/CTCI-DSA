# Queue implementation using deque
from collections import deque


class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.appendleft(data)

    def dequeue(self):
        try:
            return self.queue.pop()
        except IndexError:
            print("Queue is empty")

    def is_empty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
q.dequeue()             # IndexError exception caught
