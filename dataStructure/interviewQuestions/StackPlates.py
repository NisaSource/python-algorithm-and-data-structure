

class PlateStack():
    def __init__(self, maxPlate):
        self.maxPlate = maxPlate
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, val):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.maxPlate:
            self.stacks[-1].append(val)
        else:
            self.stacks.append([val])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def popAt(self, stackNum):
        if len(self.stacks[stackNum]) > 0:
            return self.stacks[stackNum].pop()
        else:
            return None

stackPlate = PlateStack(3)
stackPlate.push(3)
stackPlate.push(5)
stackPlate.push(6)
stackPlate.push(8)

print(stackPlate.popAt(1))
