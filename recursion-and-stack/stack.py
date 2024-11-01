class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack: #it's same with Linked List
    def __init__(self):
        self.head = None
    
    def push(self, value):
        next = self.head
        self.head = Node(value)
        self.head.next = next
        return
    
    @property    
    def pop(self):
        value = self.head.value
        self.head = self.head.next
        return value
    
    @property
    def is_empty(self):
        return self.head is None

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
    
stack_obj = Stack()

stack_obj.push("Monday")
stack_obj.push("Tuesday")
stack_obj.push("Wednesday")
stack_obj.push("Thursday")
stack_obj.push("Friday")
stack_obj.push("Saturday")
stack_obj.push("Sunday")

# stack_obj.print_all
print(stack_obj.pop)
print(stack_obj.peek)