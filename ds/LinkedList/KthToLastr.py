# Return the Kth to last element from a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def KthLastElement(node, k):
    # Approach 1
    # Set a counter = k
    # For every node, traverse k nodes such that the kth node should be NULL if it is the required node
    # counter = k
    # p = node
    # while(p != None):
    #     counter = k
    #     ans = p
    #     while(counter != 0):
    #         p = p.next
    #         counter -= 1
    #     if(p == None):
    #         return(ans.data)
    #     p = ans.next
    #
    #  Approach 2
    #  Traverse through the linked list and determinee the length of the list
    #  Print the value of the element present at LENGTH - K index
    #
    #  Approach 3
    #  Take 2 pointers - p1 and p2
    #  p1 is at start node and p2 is placed K nodes ahead of p1
    #  Move them at the same pace
    #  If p2 == NULL then p1 will be at the required node
    p1 = node
    p2 = node
    for i in range(k):
        if(p2 == None):
            return("K is out of range")
        p2 = p2.next

    while(p2 != None):
        p1 = p1.next
        p2 = p2.next
    return(str(k) + "th node from the end is " + str(p1.data))


def DisplayLlist(node):
    current = node
    while(current != None):
        print(current.data, end="->")
        current = current.next
    print("NULL")


n1 = Node(10)
n1.next = Node(20)
n1.next.next = Node(30)
n1.next.next.next = Node(45)
n1.next.next.next.next = Node(57)
n1.next.next.next.next.next = Node(60)
n1.next.next.next.next.next.next = Node(70)
n1.next.next.next.next.next.next.next = Node(80)
n1.next.next.next.next.next.next.next.next = None
DisplayLlist(n1)
print(KthLastElement(n1, 1))
print(KthLastElement(n1, 2))
print(KthLastElement(n1, 3))
print(KthLastElement(n1, 4))
print(KthLastElement(n1, 5))
print(KthLastElement(n1, 6))
print(KthLastElement(n1, 7))
print(KthLastElement(n1, 8))
print(KthLastElement(n1, 9))
