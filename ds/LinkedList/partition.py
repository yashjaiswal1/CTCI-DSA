# Partition the given linked list around the pivot (order of the elements is not of concern)
class LinkedList:
    head = None

    def append(self, new):
        if(self.head == None):
            self.head = new
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = new

    def prepend(self, new):
        if(self.head == None):
            self.head = new
        else:
            temp = self.head
            self.head = new
            self.head.next = temp

    def displayList(self):
        if(self.head == None):
            print("List is empty!")
        else:
            current = self.head
            while(current != None):
                print(current.data, end="->")
                current = current.next
            print("NULL")
# Partition the given linked list around the pivot (order of the elements is not of concern)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def partition(head, key):
    if head == None:
        print("List is empty. Partition not possible.")
    else:
        current = head
        left = LinkedList()
        right = LinkedList()
        while(current != None):
            if(current.data < key):
                left.prepend(Node(current.data))
            else:
                right.prepend(Node(current.data))
            current = current.next
        temp = left.head
        while(temp.next != None):
            temp = temp.next
        temp.next = right.head
        left.displayList()


# n1 = Node(70)
# n1.next = Node(70)
# n1.next.next = Node(40)
# n1.next.next.next = Node(25)
# n1.next.next.next.next = Node(27)
# n1.next.next.next.next.next = Node(0)
# n1.next.next.next.next.next.next = Node(0)
# n1.next.next.next.next.next.next.next = Node(0)
# n1.next.next.next.next.next.next.next.next = None
# DisplayLlist(n1)
# partition(n1, 30)
# DisplayLlist(n1)
llist = LinkedList()
llist.append(Node(10))
llist.append(Node(30))
llist.append(Node(20))
llist.append(Node(40))
llist.append(Node(15))
llist.append(Node(90))
llist.displayList()
partition(llist.head, 40)
