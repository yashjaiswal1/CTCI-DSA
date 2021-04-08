# Queue implementation using lists
class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return (len(self.queue) == 0)

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)


q = Queue()
print(q.is_empty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.dequeue()             # Queue is empty
