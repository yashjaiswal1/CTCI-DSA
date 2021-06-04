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
        Returns a reference to the required node if the key is matched,
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

    def inOrder(self, localRoot):
        # inorder will give an ascending order only if the tree is a BST!
        if localRoot != None:
            self.inOrder(localRoot.leftChild)
            print("Visited node " + str(localRoot.idata))
            self.inOrder(localRoot.rightChild)

    def preOrder(self, localRoot):
        if localRoot != None:
            print("Visited node " + str(localRoot.idata))
            self.preOrder(localRoot.leftChild)
            self.preOrder(localRoot.rightChild)

    def postOrder(self, localRoot):
        if localRoot != None:
            self.postOrder(localRoot.leftChild)
            self.postOrder(localRoot.rightChild)
            print("Visited node " + str(localRoot.idata))


n1 = Node(10, 10)
n2 = Node(5, 20)
n3 = Node(20, 30)
n1.leftChild = n2
n1.rightChild = n3
mytree = Tree()
mytree.root = n1
mytree.insert_node(15, 40)
mytree.insert_node(25, 50)
answer = mytree.find_key(25)
print(answer.idata, answer.fdata)

print("\nINORDER TRAVERSAL")
mytree.inOrder(mytree.root)

print("\nPREORDER TRAVERSAL")
mytree.preOrder(mytree.root)

print("\nPOSTORDER TRAVERSAL")
mytree.postOrder(mytree.root)
