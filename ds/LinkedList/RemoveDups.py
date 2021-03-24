# Remove duplicates from an unsorted linked list without using a temporary buffer
# Remove first occurence of the duplicate only

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def RemoveDups(node):
    p1 = node
    while(p1 != None):
        p2 = p1
        while(p2.next != None):
            if(p2.next.data == p1.data):
                p2.next = p2.next.next
            else:
                p2 = p2.next
        p1 = p1.next


def DisplayLlist(node):
    current = node
    while(current != None):
        print(current.data, end="->")
        current = current.next
    print("NULL")


n1 = Node(70)
n1.next = Node(70)
n1.next.next = Node(40)
n1.next.next.next = Node(25)
n1.next.next.next.next = Node(27)
n1.next.next.next.next.next = Node(0)
n1.next.next.next.next.next.next = Node(0)
n1.next.next.next.next.next.next.next = Node(0)
n1.next.next.next.next.next.next.next.next = None
DisplayLlist(n1)
RemoveDups(n1)
DisplayLlist(n1)
