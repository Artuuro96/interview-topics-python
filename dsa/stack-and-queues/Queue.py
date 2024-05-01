from Node import Node


# first -> 1 <- last

class Queue:
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def add(self, value):
        new_node = Node(value)
        if self.last is not None:
            self.last.nxt = new_node

        self.last = new_node

        if self.first is None:
            self.first = self.last

    def print_queue(self):
        queue_str = "[first]"
        while self.first is not None:
            queue_str += "->" + str(self.first.value)
            self.first = self.first.nxt

        print(f"{queue_str}->[last]")

    def remove(self):
        if self.is_empty():
            print("Empty Queue")
            return
        self.first = self.first.nxt
        if self.first.nxt is None:
            self.last = self.first

    def peek(self):
        if self.is_empty():
            print("Empty Queue")
            return
        return self.first.value

    def is_empty(self):
        if self.first is None:
            return True
        return False


queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.remove()
queue.add(5)

queue.print_queue()
