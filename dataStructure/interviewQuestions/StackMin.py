# Design a stack which in addition to push and pop, has a function min
# which returns the minimum element (Push, pop, and min should be O(1))

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = str(self.val)
        if self.next:
            s += "," + str(self.next)
        return s

class Stack():
    def __init__(self):
        self.top = None
        self.minVal = None

    def min(self):
        if not self.minVal:
            return None
        return self.minVal.val
    
    def push(self, n):
        if self.minVal and (self.minVal.val < n):
            self.minVal = Node(val = self.minVal.val, next=self.minVal)
        else:
            self.minVal = Node(val = n, next = self.minVal)
        self.top = Node(val = n, next = self.top)

    def pop(self):
        if not self.top:
            return None
        self.minVal = self.minVal.next
        n = self.top.val
        self.top = self.top.next
        return n

stackMin = Stack()
stackMin.push(4)
print(stackMin.min())
stackMin.push(5)
print(stackMin.min())
stackMin.push(6)
print(stackMin.min())
stackMin.push(3)
print(stackMin.min())
stackMin.push(6)
print(stackMin.min())
stackMin.push(1)
print(stackMin.min())