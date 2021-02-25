# Create a Queue class which implements a queue using 2 stacks

class Stack():
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, val):
        self.list.append(val)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()

class Queue():
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, val):
        self.inStack.push(val)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        res = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return res

queueStack = Queue()
queueStack.enqueue(6)
queueStack.enqueue(7)
queueStack.enqueue(8)
queueStack.enqueue(9)
print(queueStack.dequeue())
queueStack.enqueue(10)
print(queueStack.dequeue())
