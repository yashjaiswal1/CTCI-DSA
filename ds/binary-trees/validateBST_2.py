# Approach 2 for validate BSTS using InOrder method
# We carry out inorder traversal and compare each successive elements to ensure they're in sorted order

class Node:

    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


def valiadateBST(localRoot):

    if localRoot == None:
        return True

    else:
        if not valiadateBST(localRoot.leftChild):
            return False

        global last_printed
        if last_printed != None and localRoot.key <= last_printed:
            return False
        last_printed = localRoot.key

        if not valiadateBST(localRoot.rightChild):
            return False

        return True


last_printed = None
tree_root = Node(20)
tree_root.leftChild = Node(10)
tree_root.rightChild = Node(30)
tree_root.leftChild.leftChild = Node(5)
tree_root.leftChild.rightChild = Node(15)
tree_root.leftChild.rightChild.rightChild = Node(16)
tree_root.leftChild.rightChild.rightChild.rightChild = Node(17)
tree_root.rightChild.leftChild = Node(25)
tree_root.rightChild.rightChild = Node(35)

print(valiadateBST(tree_root))
