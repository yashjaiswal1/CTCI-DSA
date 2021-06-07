class Node:
    def __init__(self, key=None):
        self.key = key
        self.leftChild = None
        self.rightChild = None


def isBST(localRoot, min, max_):
    if localRoot == None:
        return True
    else:
        min_max_condition = (min != None and localRoot.key <= min) or (
            max_ != None and localRoot.key > max_)
        if min_max_condition:
            return False
        elif isBST(localRoot.leftChild, min, localRoot.key) and isBST(localRoot.rightChild, localRoot.key, max_):
            return True
        else:
            return False


tree_root = Node(20)
tree_root.leftChild = Node(10)
tree_root.rightChild = Node(30)
tree_root.leftChild.leftChild = Node(5)
tree_root.leftChild.rightChild = Node(15)
tree_root.leftChild.rightChild.rightChild = Node(16)
tree_root.leftChild.rightChild.rightChild.rightChild = Node(47)
tree_root.rightChild.leftChild = Node(25)
tree_root.rightChild.rightChild = Node(35)
print(isBST(tree_root, None, None))

#         20
#     10      30
#    5  15   25 35
#         16
#          17
