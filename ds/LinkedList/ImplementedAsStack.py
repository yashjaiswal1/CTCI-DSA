# Stack implementation of Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    top = Node(-1)

    def push(self, data):
        if(self.top.next == None):
            self.top.next = Node(data)
        else:
            temp = self.top.next
            self.top.next = Node(data)
            self.top.next.next = temp

    def pop(self):
        if(self.top.next == None):
            print("Linked list is empty!")
        else:
            temp = self.top.next
            self.top.next = self.top.next.next
            print("Node with value " + str(temp.data) + " has been popped!")

    def display(self):
        if(self.top.next == None):
            print("Linked list is empty!")
        else:
            current = self.top.next
            while(current != None):
                print(current.data)
                current = current.next


llist = LinkedList()
llist.push(10)
llist.push(20)
llist.display()
llist.push(30)
llist.display()
llist.pop()
llist.pop()
llist.pop()
llist.pop()
