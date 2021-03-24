# Implementation of linked list as queues
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    front = rear = None

    # Add a new node and move rear to the next new node
    def enQueue(self, data):
        if(self.rear == None):
            self.rear = self.front = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next

    # Remove the first node and move the first pointer to the next node
    def deQueue(self):
        if(self.front == None):
            print("Queue is empty")
        else:
            self.front = self.front.next
        if(self.front == None):
            self.rear == None

    def display(self):
        if(self.front == None):
            print("Queue is empty")
        else:
            current = self.front
            while(current != None):
                print(current.data)
                current = current.next


q = Queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.display()
q.deQueue()
q.display()
