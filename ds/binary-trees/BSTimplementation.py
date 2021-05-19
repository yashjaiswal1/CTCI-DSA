# Binary Search Tree implementation using references

# Tree node basic structure
class Node:
    def __init__(self, idata, fdata):
        self.idata = idata
        self.fdata = fdata
        self.leftChild = None
