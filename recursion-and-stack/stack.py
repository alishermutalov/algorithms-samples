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
    
    @property    
    def pop(self):
        value = self.head.value
        self.head = self.head.next
        return value
    
    @property
    def is_empty(self):
        return self.head is None
    
    @property
    def is_full(self):
        return False #It means There is no limit

    @property
    def peek(self):
        return self.head.value
    
    @property
    def print_all(self):
        item: Node = self.head
        while item:
            print(item.value)
            item = item.next
        return