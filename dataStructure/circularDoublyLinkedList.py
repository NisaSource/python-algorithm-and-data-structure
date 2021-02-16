class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Create the list
    def createList(self, nodeVal):
        newNode = Node(nodeVal)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "CREATED SUCCESSFULLY!"

    # Add node to the list
    def addNode(self, val, loc):
        if self.head is None:
            return "LIST DOESN'T EXIST!"
        else:
            newNode = Node(val)
            if loc == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif loc == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                temp = self.head
                idx = 0
                while idx < loc-1:
                    temp = temp.next
                    idx += 1
                newNode.next = temp.next
                newNode.prev = temp
                newNode.next.prev = newNode
                temp.next = newNode
            return "SUCCESSFULLY ADDED!"

    # Iterate over the list
    def iterateList(self):
        if self.head is None:
            print("NO NODE TO ITERATE")
        else:
            temp = self.head
            while temp:
                print(temp.value)
                if temp == self.tail:
                    break
                temp = temp.next

    # Reverse the node in the list
    def reverseNode(self):
        if self.head is None:
            print("NO NODE TO REVERSE")
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                if temp == self.head:
                    break
                temp = temp.prev

    # Find node in the list
    def findNode(self, nodeVal):
        if self.head is None:
            return "NO NODE IN THE LIST"
        else:
            temp = self.head
            while temp:
                if temp.value == nodeVal:
                    return temp.value
                if temp == self.tail:
                    return "NODE DOESN'T EXIST"
                temp = temp.next

    # Remove node from the list
    def removeNode(self, loc):
        if self.head is None:
            print("NO NODE TO REMOVE")
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif loc == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                current = self.head
                idx = 0
                while idx < loc-1:
                    current = current.next
                    idx += 1
                current.next = current.next.next
                current.next.prev = current
            print("SUCCESSFULLY DELETED!")

    # Remove the list
    def removeList(self):
        if self.head is None:
            print("NO ELEMENT TO REMOVE")
        else:
            self.tail.next = None
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
            print("LIST SUCCESSFULLY DELETED!")            




    
circularDLL = CircularDoublyLL()
print(circularDLL.createList(7))
circularDLL.addNode(0,0)
circularDLL.addNode(1,1)
circularDLL.addNode(2,2)

print([node.value for node in circularDLL])

circularDLL.iterateList()
print([node.value for node in circularDLL])
circularDLL.reverseNode()
print(circularDLL.findNode(7))
print(circularDLL.findNode(8))
circularDLL.removeNode(2)
print([node.value for node in circularDLL])
circularDLL.removeList()
print([node.value for node in circularDLL])
