# Linked List Runner Technique
# Given: a linked list a1->a2->a3->b1->b2->b3 of even length
# Outcome: a1->b1->a2->b2->a3->b3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def RunnerMethod(node):
    p1 = node
    p2 = node.next
    while(p2.next != None):
        p1 = p1.next
        p2 = p2.next.next

    p2 = node
    while(p1 != p2):
        # Isolate the target node first
        target = p1.next
        p1.next = p1.next.next
        target.next = None
        # Now, add target node after p2
        temp = p2.next
        p2.next = target
        p2.next.next = temp
        p2 = p2.next.next


def DisplayLlist(node):
    current = node
    while(current != None):
        print(current.data, end="->")
        current = current.next
    print("NULL")


n1 = Node(10)
n1.next = Node(20)
n1.next.next = Node(30)
n1.next.next.next = Node(60)
n1.next.next.next.next = Node(70)
n1.next.next.next.next.next = Node(80)
n1.next.next.next.next.next.next = None
RunnerMethod(n1)
DisplayLlist(n1)
