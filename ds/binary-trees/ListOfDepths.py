# APPROACH:
# if localRoot != None:
#   llist.append(Node())
#   llist[level].push(Node(localRoot.key))
#   level += 1
#   func(localRoot.leftChild, llist, level)
#   func(localRoot.rightChildm llist, level)
#   level -= 1
# return None

class TreeNode:
    def __init__(self, key=None):
        self.key = key
        self.leftChild = None
        self.rightChild = None


class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head        # 'head' is Node class-type variable

    def push(self, key):
        if self.head == None:
            self.head = Node(key)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(key)

    def displayList(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            current = self.head
            while current != None:
                print(current.key, end=" -> ")
                current = current.next
            print("None\n")


def createDepthLists(localRoot, array_list, level):
    if localRoot != None:

        if len(array_list) == level:
            new_node = Node(localRoot.key)
            llist = LinkedList(new_node)
            array_list.append(llist)

        else:
            array_list[level].push(localRoot.key)
        createDepthLists(localRoot.leftChild, array_list, level+1)
        createDepthLists(localRoot.rightChild, array_list, level+1)
    else:
        return


tree_root = TreeNode(20)
tree_root.leftChild = TreeNode(10)
tree_root.rightChild = TreeNode(30)
tree_root.leftChild.leftChild = TreeNode(5)
tree_root.leftChild.rightChild = TreeNode(15)
tree_root.rightChild.leftChild = TreeNode(25)
tree_root.rightChild.rightChild = TreeNode(35)
array_list = []
createDepthLists(tree_root, array_list, 0)

for level in range(3):
    array_list[level].displayList()
