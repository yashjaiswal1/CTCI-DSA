# Implement a queue using 2 stacks
# 2 stacks
# Assuming no stack capacity limit is required here
# __init__() -> initialize 2 stacks
# push -> normal
# pop, peek -> modified

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def isEmpty(self):
        return self.stack1 == []

    def transferStackElements(self, stack1, stack2):
        """
        Pops all elements from stack1 and appends them into stack2 such that stack2 is the reverse of stack1.
        """
        while stack1 != []:
            stack2.append(stack1.pop())

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            self.transferStackElements(stack1=self.stack1, stack2=self.stack2)
            removed_element = self.stack2.pop()
            self.transferStackElements(stack1=self.stack2, stack2=self.stack1)
            return removed_element

    def peekFront(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            self.transferStackElements(stack1=self.stack1, stack2=self.stack2)
            print(self.stack2[-1])
            self.transferStackElements(stack1=self.stack2, stack2=self.stack1)

    def peekRear(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            print(self.stack1[-1])


queue_ = MyQueue()
queue_.dequeue()
queue_.enqueue(10)
queue_.enqueue(20)
queue_.enqueue(30)
queue_.enqueue(40)
print(queue_.stack1)
queue_.peekFront()
queue_.peekRear()
queue_.dequeue()
print(queue_.stack1)
queue_.dequeue()
print(queue_.stack1)
queue_.dequeue()
print(queue_.stack1)
queue_.dequeue()
print(queue_.stack1)
queue_.dequeue()
