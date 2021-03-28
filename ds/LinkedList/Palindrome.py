# Determine if the given linked list is a palindrome or not
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    head = None

    def append(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = Node(data)

    def displayList(self):
        if(self.head == None):
            print("The linked list is empty!")
            return
        else:
            current = self.head
            while(current != None):
                print(current.data, end=" -> ")
                current = current.next
            print("None")


def IsPalindrome(llist):
    # (1) Use the runner technique to find the middle node
    # (1.5) Meanwhile, keep storing the nodes from slower pointer into a STACK
    # (2) Faster node reaches NULL (end)
    # (3) Compare the slower node (now in the middle) with the Top of the STACK
    # (4) If no mismatch then return True
    # (5) If mismatch occurs then return False
    # [] -> [] -> [] -> NULL
    # [] -> [] -> [] -> [] -> NULL
    runner_node = llist.head
    slower_node = llist.head
    stack = []
    while runner_node and runner_node.next:
        stack.append(slower_node.data)
        slower_node = slower_node.next
        runner_node = runner_node.next.next
    if runner_node:
        slower_node = slower_node.next

    while(slower_node != None):
        if(slower_node.data != stack.pop()):
            return False
        slower_node = slower_node.next
    return True


list1 = LinkedList()
list1.append(10)
list1.append(20)
list1.append(20)
list1.append(10)

print(IsPalindrome(list1))
