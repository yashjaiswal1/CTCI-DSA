# two numbers are stored in 2 linked lists such that the head has the one's digit and so on...
# return their sum in a linked list
# Approach:
# (1) Add the first nodes from both lists along with the carry variable (init. value = 0)
# (2) If the resultant sum is a 1 digit number then write it to the first node of the sum list
# (3) If the resultant sum is a 2 digit number then write the one's digit of the sum to the first node of sum list
#     and put carry = sum's ten's digit
# (4) If we're at last node and resultant sum is a 2-digit number then write one's digit in the current sum list node
#     and ten's digit in the next sum list node
# (5) Repeat the above steps for rest of the numbers until we reach NULL in the linked list

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


def sumLists(llist1, llist2):
    result = LinkedList()
    ptr1 = llist1.head
    ptr2 = llist2.head
    ptr3 = result
    carry = 0
    sum_of_nodes = 0
    while(ptr1 != None and ptr2 != None):
        if(ptr1):
            sum_of_nodes += ptr1.data
            ptr1 = ptr1.next
        if(ptr2):
            sum_of_nodes += ptr2.data
            ptr2 = ptr2.next
        sum_of_nodes += carry
        print(sum_of_nodes)
        if(len(str(sum_of_nodes)) == 1):
            ptr3.append(sum_of_nodes)
            carry = 0
        elif(len(str(sum_of_nodes)) == 2 and ptr1 == None):
            ptr3.append(int(sum_of_nodes % 10))
            ptr3.append(int(sum_of_nodes // 10))
        else:
            ptr3.append(int(sum_of_nodes % 10))
            carry = int(sum_of_nodes // 10)
    return result


Number1 = LinkedList()
Number1.append(0)
Number1.append(1)
Number2 = LinkedList()
Number2.append(5)
result_list = sumLists(Number1, Number2)
result_list.displayList()
