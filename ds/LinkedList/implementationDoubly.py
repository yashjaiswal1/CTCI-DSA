# Check again!!!
# Implementation of Doubly Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data)
            current.next.prev = current

    def prepend(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev

    def insertElement(self, data, position):  # Inserts element after Kth position
        if self.head == None:
            self.head = Node(data)
        else:
            counter = 0
            current = self.head
            while counter != position:
                current = current.next
                counter += 1
            temp = current.next
            current.next = Node(data)
            current.next.prev = current
            current.next.next = temp
            temp.prev = current.next

    def deleteElement(self, position):  # Deletes element at Kth position
        if self.head == None:
            print("Linked list is empty!")
            return
        elif self.head.next == None:
            self.head = None
        else:
            counter = 0
            current = self.head
            while counter != position:
                current = current.next
                counter += 1
            temp = current
            temp.prev.next = current.next
            temp.next.prev = current.prev
            current.next = None
            current.prev = None

    def printLinkedList(self):
        if self.head == None:
            print("Linked list is empty!")
        else:
            current = self.head
            while current.next != None:
                print(current.data)
                current = current.next
            print(current.data)


DLlist = DoublyLinkedList()
# DLlist.append(10)
# DLlist.append(20)
# DLlist.append(30)
# DLlist.append(40)
# DLlist.append(50)
# DLlist.append(60)
# DLlist.printLinkedList()
# DLlist.insertElement(45, 3)
# DLlist.printLinkedList()
# DLlist.deleteElement(2)
# DLlist.printLinkedList()
DLlist.append(10)
DLlist.append(20)
DLlist.printLinkedList()
DLlist.deleteElement(1)
DLlist.printLinkedList()
