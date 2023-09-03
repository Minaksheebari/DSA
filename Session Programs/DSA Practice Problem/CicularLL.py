# Create a Python class for a circular linked list and include methods for insertion, deletion, and traversal. 
# Demonstrate how to add elements to and remove elements from a circular linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the end of the circular linked list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Deletion of a node by value
    def delete(self, value):
        if not self.head:
            return

        if self.head.data == value:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
        else:
            prev = None
            current = self.head
            while current.next != self.head:
                if current.data == value:
                    prev.next = current.next
                    return
                prev = current
                current = current.next

    # Traversal of the circular linked list
    def traverse(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

# Demonstration
cll = CircularLinkedList()

# Insert elements
cll.insert(1)
cll.insert(2)
cll.insert(3)

# Traverse and print
print("Circular Linked List:")
cll.traverse()  # Output: 1 -> 2 -> 3 ->

# Delete element
cll.delete(2)

# Traverse and print after deletion
print("Circular Linked List after deletion:")
cll.traverse()  # Output: 1 -> 3 ->
