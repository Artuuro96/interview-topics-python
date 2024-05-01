from Node import Node


#  null <- 1
#            <- 2 == TOP
class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        new_top = Node(value)
        new_top.nxt = self.top
        self.top = new_top

    def pop(self):
        if self.is_empty():
            print("Empty Stack")
            return
        val = self.top.value
        self.top = self.top.nxt
        return val

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def print_stack(self):
        while self.top is not None:
            print(self.top.value)
            self.top = self.top.nxt


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.print_stack()
