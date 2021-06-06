# Approach:
# minTree(arr)
# (1) Calculate middle element of input array
# (2) set it's left and right child
# (3) left = minTree(arr[0:mid-1])
# (4) right = minTree(arr[mid+1 : ])
# (5) BASE CASE: if low > high
# (6) insert mid into the tree at every step

class Node:
    def __init__(self, key=None):
        self.key = key
        self.leftChild = None
        self.rightChild = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
            return self.root
        else:
            current = self.root
            isLeft = True
            parent = None
            while current != None:
                parent = current
                if key < current.key:
                    isLeft = True
                    current = current.leftChild
                elif key > current.key:
                    isLeft = False
                    current = current.rightChild

            if isLeft:
                parent.leftChild = Node(key)
                return parent.leftChild
            else:
                parent.rightChild = Node(key)
                return parent.rightChild


def minTree(arr, low, high):
    if low > high:
        return None
    else:
        mid = (low + high) // 2
        # new_node = tree.insert(arr[mid])
        # Notice that instead of pushing nodes to a pre-built tree, we are just creating a node in
        # each recursive step along with it's left and right pointers set.
        # At the end, we return the newly created node (which ultimately becomes our root node)
        new_node = Node(arr[mid])
        new_node.leftChild = minTree(arr, low, mid-1)
        new_node.rightChild = minTree(arr, mid+1, high)
        return new_node


input_arr = [1, 2, 3, 4, 5, 6]
root_node = minTree(input_arr, 0, 5)
print(root_node.key)
print(root_node.leftChild.key)
print(root_node.rightChild.key)
