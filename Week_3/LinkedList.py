#LinkedList
class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def inseertAtBeginning(self, data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node

    def insert(self, data):
        new_Node = Node(data)
        if(self.head is None):
            self.head = new_Node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_Node

    def insertAtPosition(self, data, position):
        new_Node = Node(data)
        if(position == 0):
            new_Node.next = self.head
            self.head = new_Node
        else:
            current = self.head
            count = 0
            while(current and count < position-1):
                current = current.next
                count += 1
                if(current is None):
                    return "Position is not in the list"
                new_Node.next = current.next
                current.next = new_Node
    def delete(self, key):
        current = self.head
        previous = None
        while(current and current.data != key):
            previous = current
            current = current.next
        if(current is None):
            return "Key is not found"
        if(previous is None):
            self.head = current.next    
        else:
            previous.next = current.next
        
    def display(self):
        current = self.head
        while(current):
            print(current.data, end=" ")
            current = current.next

l = LinkedList()
l.insert(1)    
l.insert(2)
l.insert("Sathish")
l.inseertAtBeginning(0)
l.delete(2)
l.insertAtPosition(5, 2)
l.display()

#doubly linked list
class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__ (self):
        self.head = None
    def insert(self,data):
        new_Node = Node(data)
        if(self.head is None):
            self.head = new_Node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_Node
            new_Node.prev = current
    def insertAtBeginning(self, data):
        new_Node = Node(data)
        if(self.head is None):
            self.head = new_Node
        else:
            new_Node.next = self.head
            self.head.prev = new_Node
            self.head = new_Node

    def display(self):          
        current = self.head
        while(current):
            print(current.data, end=" ")
            current = current.next
dl = DoublyLinkedList()
dl.insert(1)       
dl.insert(2)
dl.insert("Sathish")
dl.insertAtBeginning(0)    
dl.display()

