#. Implement three stacks using a single list

class MultiStack:
    def __init__(self, sz):
        self.stacksNum = 3
        self.stackList = [0] * (sz * self.stacksNum)
        self.sizes = [0] * self.stacksNum
        self.sz = sz

    def isFull(self, n):
        if self.sizes[n] == self.sz:
            return True
        else:
            return False
        
    def isEmpty(self, n):
        if self.sizes[n] == 0:
            return True
        else:
            return False
        
    def topIndex(self, n):
        offset = n * self.sz
        return offset + self.sizes[n] - 1
    
    def push(self, item, n):
        if self.isFull(n):
            return "Stack is FULL"
        else:
            self.sizes[n] += 1
            self.stackList[self.topIndex(n)] = item

    def pop(self, n):
        if self.isEmpty(n):
            return "The stack is EMPTY"
        else:
            val = self.stackList[self.topIndex(n)]
            self.stackList[self.topIndex(n)] = 0
            self.sizes[n] -= 1
            return val

    def peek(self, n):
        if self.isEmpty(n):
            return "The stack is EMPTY"
        else:
            return self.stackList[self.topIndex(n)]


multiStack = MultiStack(8)
print(multiStack.isFull(0))
print(multiStack.isEmpty(1))
multiStack.push(1,0)
multiStack.push(2,0)
multiStack.push(3,2)
print(multiStack.pop(0))