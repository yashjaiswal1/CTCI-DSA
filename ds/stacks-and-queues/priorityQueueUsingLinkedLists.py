from typing import Sized


class Item:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.header_node = None

    def enqueue(self, item):
        if self.header_node == None:
            self.header_node = item
        else:
            current = self.header_node
            last = Item(None, None)
            while current != None:
                if current.priority < item.priority:
                    last.next = item
                    item.next = current
                    if current == self.header_node:
                        self.header_node = item
                    return
                last = current
                current = current.next
            last.next = item

    def dequeue(self):
        if self.header_node == None:
            print("Priority Queue is empty!")
        else:
            temp = self.header_node
            self.header_node = self.header_node.next
            return temp.data

    def printQueue(self):
        current = self.header_node
        while current != None:
            print(current.data)
            current = current.next


pq = PriorityQueue()
pq.dequeue()
pq.enqueue(Item(10, 10))
pq.enqueue(Item(20, 20))
pq.enqueue(Item(30, 30))
pq.enqueue(Item(15, 15))
pq.enqueue(Item(0, 0))
pq.printQueue()
print("Popped = ", pq.dequeue())
print("Popped = ", pq.dequeue())
print("Popped = ", pq.dequeue())
pq.printQueue()
print("Popped = ", pq.dequeue())
print("Popped = ", pq.dequeue())
print("Popped = ", pq.dequeue())
