# Implementation of circular queue using lists
class CircularQueue:

    def __init__(self, size):
        self.cqueue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def is_empty(self):
        if(self.front == -1 and self.rear == -1):
            return True
        else:
            return False

    def enqueue(self, data):
        is_cqueue_full = ((self.front == 0 and self.rear ==
                           self.size - 1) or (self.rear == self.front - 1))
        # ALTERNATE CONDITION: ((self.rear + 1) % self.size == self.front)

        if is_cqueue_full:
            print("Circular Queue is full!")
        else:
            if(self.is_empty()):
                self.rear = self.front = 0
            else:
                self.rear += 1
                self.rear = self.rear % self.size
            self.cqueue[self.rear] = data

    def dequeue(self):
        is_cqueue_empty = self.is_empty()
        if(is_cqueue_empty):
            print("Circular Queue is empty!")
        else:
            temp = self.cqueue[self.front]
            self.cqueue[self.front] = None
            if(self.front == self.rear):
                self.front = self.rear = -1
            else:
                self.front += 1
                self.front = self.front % self.size
            return temp

    def get_cqueue(self):
        return self.cqueue


circular_queue_instance = CircularQueue(5)
# circular_queue_instance.enqueue(10)
# circular_queue_instance.enqueue(20)
# circular_queue_instance.enqueue(30)
# circular_queue_instance.enqueue(40)
# circular_queue_instance.enqueue(50)
# circular_queue_instance.enqueue(99)
# print(circular_queue_instance.get_cqueue())
# print(circular_queue_instance.dequeue())
# print(circular_queue_instance.dequeue())
# print(circular_queue_instance.dequeue())
# print(circular_queue_instance.dequeue())
# print(circular_queue_instance.dequeue())
# print(circular_queue_instance.dequeue())        # pritns None too
# print(circular_queue_instance.get_cqueue())
# print(circular_queue_instance.is_empty())
circular_queue_instance.enqueue(10)
circular_queue_instance.enqueue(20)
circular_queue_instance.enqueue(30)
circular_queue_instance.enqueue(40)
circular_queue_instance.dequeue()
circular_queue_instance.dequeue()
print(circular_queue_instance.get_cqueue())
circular_queue_instance.enqueue(50)
circular_queue_instance.enqueue(60)
circular_queue_instance.enqueue(70)
circular_queue_instance.enqueue(80)             # Circular queue is full
print(circular_queue_instance.get_cqueue())
