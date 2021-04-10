class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front == None and self.rear == None:
            return True
        else:
            return False

    def enqueue(self, data):
        temp = Node(data)
        if self.is_empty():
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.rear.next = self.front

    def dequeue(self):
        if self.is_empty():
            print("Circular queue is empty!")
        elif self.front == self.rear:
            self.front = self.rear = None
        else:
            temp = self.front.next
            self.front = None
            self.rear.next = temp
            self.front = temp

    def printCircularQueue(self):
        if(self.is_empty()):
            print("Circular Queue is empty!")
        else:
            current = self.front
            while(current.next != self.front):
                print(current.data)
                current = current.next
            print(current.data)


circular_queue = CircularQueue()
circular_queue.dequeue()
circular_queue.enqueue(10)
circular_queue.enqueue(20)
circular_queue.enqueue(30)
circular_queue.enqueue(40)
circular_queue.enqueue(50)
circular_queue.printCircularQueue()
circular_queue.dequeue()
circular_queue.dequeue()
circular_queue.printCircularQueue()
circular_queue.dequeue()
circular_queue.dequeue()
circular_queue.dequeue()
circular_queue.printCircularQueue()
