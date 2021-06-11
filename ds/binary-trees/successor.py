class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.leftChild = None
        self.rightChild = None


def getLeftmostElement(node):
    successor = None
    successorParent = node
    current = node.rightChild
    while current.leftChild != None:
        successorParent = current
        current = current.leftChild
    successor = current

    return successor


def getSuccessor(node):
    if node == None:
        return None
    else:
        if node.rightChild != None:
            successor = getLeftmostElement(node)
            return successor
        else:
            current = node
            parent = node.parent
            while parent != None and parent.leftChild != current:
                current = parent
                parent = parent.parent
            return parent


tree_root = Node(10, None)
tree_root.leftChild = Node(5, tree_root)
tree_root.rightChild = Node(15, tree_root)
print(getSuccessor(tree_root).key)
