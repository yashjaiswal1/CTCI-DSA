class Node:
    def __init__(self, key=None):
        self.key = key
        self.leftChild = None
        self.rightChild = None


def isBalanced(localRoot):
    if localRoot == None:
        return True
    else:
        difference = abs(getHeight(localRoot.leftChild) -
                         getHeight(localRoot.rightChild))
        if difference > 1:
            return False
        elif isBalanced(localRoot.leftChild) and isBalanced(localRoot.rightChild):
            return True


def getHeight(node):
    if node == None:
        return -1
    else:
        return max(getHeight(node.leftChild), getHeight(node.rightChild)) + 1


tree_root = Node(20)
tree_root.leftChild = Node(10)
tree_root.rightChild = Node(30)
tree_root.leftChild.leftChild = Node(5)
tree_root.leftChild.rightChild = Node(15)
tree_root.leftChild.rightChild.rightChild = Node(16)
tree_root.leftChild.rightChild.rightChild.rightChild = Node(17)
tree_root.rightChild.leftChild = Node(25)
tree_root.rightChild.rightChild = Node(35)
print(isBalanced(tree_root))
