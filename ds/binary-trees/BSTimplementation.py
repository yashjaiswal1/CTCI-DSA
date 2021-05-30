# Binary Search Tree implementation using references

class Node:
    def __init__(self, idata=None, fdata=None):
        self.idata = idata              # key
        self.fdata = fdata              # data value to be stored
        self.leftChild = None           # reference to left subchild
        self.rightChild = None          # reference to right subchild


class Tree:
    def __init__(self):
        self.root = None

    def find_key(self, key):
        """
        Returns a reference to the required node if the key if matched,
        else, it returns None

        Efficiency: O(log N) --- base 2 logarithm
        N -> number of data elements
        """
        current = self.root
        while current.idata != key:
            if key < current.idata:
                current = current.leftChild
            elif key > current.idata:
                current = current.rightChild
            if current == None:
                return None
        return current

    def insert_node(self, key, data):
        """
        Inserts a node in the required position as per BSTs

        Efficiency: O(log N)
        in reality, it's traversing N+1 levels. The +1 comes because it's traversing one level 
        below the last known level wherein the value is NULL but the +1 is discarded 
        because we're working with Big O notations.
        """
        new_node = Node(key, data)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            parent = Node()
            while True:
                parent = current
                if key < current.idata:
                    current = current.leftChild
                    if current == None:
                        parent.leftChild = new_node
                        return
                else:
                    current = current.rightChild
                    if current == None:
                        parent.rightChild = new_node
                        return


n1 = Node(5, 10)
n2 = Node(6, 20)
n3 = Node(4, 30)
n1.leftChild = n3
n1.rightChild = n2
mytree = Tree()
mytree.root = n1
mytree.insert_node(8, 40)
answer = mytree.find_key(8)
print(answer.idata, answer.fdata)
