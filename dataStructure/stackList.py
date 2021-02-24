class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(val) for val in self.list]
        return '\n'.join(values)

    # Create isEmpty method to check if the stack is empty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # Create push method to add value to the stack
    def push(self, val):
        self.list.append(val)
        return "Successfully added!"

    # Create pop method to pop out the value from the stack
    def pop(self):
        if self.isEmpty():
            return "No such element in the stack"
        else:
            return self.list.pop()

    # Create peek method to check the last value in the stack
    def peek(self):
        if self.isEmpty():
            return "No such element in the stack"
        else:
            return self.list[len(self.list) - 1]

    # Delete the entire stack
    # def delete(self):
    #     self.list = None


stackList = Stack()
print(stackList.isEmpty())

stackList.push(7)
stackList.push(8)
stackList.push(9)
# print(stackList.__str__())
stackList.pop()
print(stackList.peek())
# stackList.delete()
print(stackList)
