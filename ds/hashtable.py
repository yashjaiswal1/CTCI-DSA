# Hash Table implementation
# class hash_table 
#   --> constructor (size_of_hash-table)
#   --> insert(key, val) => hash(key) % array_size
#                   => check if first node is empty?
#                       => if empty, store key-value pair in first node of linked list
#                       => if not empty, check for the next empty node in the ll and store key-val pair
#   --> search(key) => compute hash(key) and use that to determine index in hash table
#                   => search through the linked list for the key and retrieve it's value
#   --> delete(key) => repeat steps as shown in search(key)
#                   => delete the node where key exists
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Initializing as an empty linked list
class LinkedList:
    def __init__(self):
        self.head = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashtable = [0]*size
        for i in range(size):
            self.hashtable[i] = LinkedList()
            self.hashtable[i].head = Node(i, None)

    def insert_key(self, key, value):
        self.temp_llist = self.hashtable[hash(key) % self.size].head
        while(self.temp_llist.next != None):
            self.temp_llist = self.temp_llist.next
        self.temp_llist.next = Node(key, value)

    def search_key(self, key):
        self.temp_llist = self.hashtable[hash(key) % self.size].head
        while(self.temp_llist.next != None):
            self.temp_llist = self.temp_llist.next
        print("Value of " + str(key) + " key is: " + str(self.temp_llist.value))

    def delete_key(self, key):
        self.temp_llist = self.hashtable[hash(key) % self.size].head
        while(self.temp_llist.next != None):
            if(self.temp_llist.next.key == key):
                self.temp_llist.next = None
                break
            self.temp_llist = self.temp_llist.next


    def display_hash_table(self):
        for i in range(self.size):
            if(self.hashtable[i].head.next != None):
                self.current_node = self.hashtable[i].head
                print(str(self.hashtable[i].head.key) + " - " + str(self.hashtable[i].head.value))
                while(self.current_node.next != None):
                    self.current_node = self.current_node.next
                    print(str(self.current_node.key) + " - " + str(self.current_node.value))
            else:
                print(str(self.hashtable[i].head.key) + " - " + str(self.hashtable[i].head.value))


ht = HashTable(5)
ht.insert_key("abc", 10)
ht.insert_key("xyz", 20)
ht.insert_key("pqr", 45)
ht.insert_key("pyz", 55)
ht.search_key("pqr")
ht.display_hash_table()
ht.delete_key("pqr")
ht.display_hash_table()
