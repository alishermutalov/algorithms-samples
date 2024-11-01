class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack: #it's same with Linked List
    def __init__(self, head):
        self.head = head
    
    def push(self, value):
        next = self.head
        self.head = Node(value)
        self.head.next = next
        
    def pop(self):
        value = self.head.value
        self.head = self.head.next
        return value
    
    def isEmpty(self):
        return self.head is None
    
    
