# Implementation for Singly-ended linked list
# Singly-ended linked list has a header node with reference to only first node
# NOTE:  I haven't added header node in this implementation.
# Doubly-ended linked list is also there. It has a header node which contains references to both - first and last nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data)

    def prepend(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = Node(data)
            current.next = self.head
            self.head = current

    def deleteFirst(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next

    def deleteLast(self):
        if self.head == None:
            return
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None

    def deleteElement(self, target):
        if self.head == None:
            return
        else:
            current = self.head
            while current.next.data != target:
                current = current.next
            current.next = current.next.next  # check

    def find_element_position(self, key):
        if(self.head == None):
            print("Linked list is empty!")
        else:
            current = self.head
            counter = 0
            while(current != None):
                if(current.data == key):
                    print("Found key at node " + str(counter))
                    return
                current = current.next
                counter += 1
            print("Key not found")

    def printLinkedList(self):
        if self.head == None:
            print("Linked List is empty!")
        else:
            current = self.head
            while current.next != None:
                print(current.data)
                current = current.next
            print(current.data)


llist = LinkedList()
llist.printLinkedList()
llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)
llist.append(50)
llist.append(60)
llist.find_element_position(40)
llist.printLinkedList()
print("Now, deleting the first and last elements of the linked list")
llist.deleteFirst()
llist.deleteLast()
llist.printLinkedList()
print("Now, deleting element with value 40")
llist.deleteElement(40)
llist.printLinkedList()
