# Approach
# (1) run through both linked lists to get their length and compare their tail nodes
# (2) move start pointer in the longer list by the difference of lengths
# (3) traverse both lists together until they colide (by reference)
# (4) return the colided node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, node):
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node


class Result:
    def __init__(self, tail, length):
        self.tail = tail
        self.length = length


def getTailAndLength(header):
    if header == None:
        return Result(None, 0)
    else:
        current = header
        length = 0
        while current.next != None:
            length += 1
            current = current.next
        length += 1
        return Result(tail=current, length=length)


def getIntersection(llist1, llist2):
    # check if have an intersection
    result1 = getTailAndLength(llist1)
    result2 = getTailAndLength(llist2)

    if result1.tail != result2.tail:
        return None

    # remove the length difference
    difference = 0
    if result1.length > result2.length:
        difference = result1.length - result2.length
        while difference != 0:
            llist1 = llist1.next
            difference -= 1

    elif result2.length > result1.length:
        difference = result2.length - result1.length
        while difference != 0:
            llist2 = llist2.next
            difference -= 1

    # traverse until collision
    while llist1 != llist2 and llist1 != None and llist2 != None:
        llist1 = llist1.next
        llist2 = llist2.next

    return None if llist1 == None or llist2 == None else llist1


n1 = Node(15)
n2 = Node(10)
n3 = Node(25)   # collision node
n4 = Node(45)
n5 = Node(-10)
list1 = LinkedList(n1)
list1.push(n2)
list1.push(n3)
list1.push(n4)
list1.push(n5)


n6 = Node(12)
n7 = Node(9)
n8 = Node(14)
n9 = Node(17)
list2 = LinkedList(n6)
list2.push(n7)
list2.push(n8)
list2.push(n9)
list2.push(n3)  # collision node

print(getIntersection(llist1=list1.head, llist2=list2.head).data)
