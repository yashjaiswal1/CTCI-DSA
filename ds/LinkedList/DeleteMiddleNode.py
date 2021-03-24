# mid-node deletion given only that node from the linked list and should not delete if it's the first or last node
# Approach
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def DeleteMidNode(node):
    if(node == None):
        print("Operation not possible")
    elif node.next == None:
        node = None
    else:
        node.data = node.next.data
        node.next = node.next.next


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
DeleteMidNode(n1.next.next.next.next.next.next.next)
DisplayLlist(n1)
