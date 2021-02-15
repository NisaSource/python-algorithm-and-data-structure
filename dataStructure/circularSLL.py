class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # Create circularly SLL
    def create(self, val):
        node = Node(val)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circularly SLL has been successfully created!"

    # Add nodes
    def add(self, val, loc):
        if self.head is None:
            return "No reference"
        else:
            newNode = Node(val)
            if loc == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif loc == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                temp = self.head
                idx = 0
                while idx < loc-1:
                    temp = temp.next
                    idx += 1
                nextNode = temp.next
                temp.next = newNode
                newNode.next = nextNode
            return "Successfully added!"

    # Iterate over CSLL
    def iterateCSLL(self):
        if self.head is None:
            print("Nothing to iterate!")
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
                if temp == self.tail.next:
                    break

    # Find the node in CSLL
    def findNode(self, nodeVal):
        if self.head is None:
            return "No node exist!"
        else:
            temp = self.head
            while temp:
                if temp.value == nodeVal:
                    return temp.value
                temp = temp.next
                if temp == self.tail.next:
                    return "Node does not exist!"

    # Remove node from CSLL
    def remove(self, loc):
        if self.head is None:
            print("No node exist!")
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif loc == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                temp = self.head
                idx = 0
                while idx < loc-1:
                    temp = temp.next
                    idx += 1
                nextNode = temp.next
                temp.next = nextNode.next

    # Delete CSLL
    def delete(self):
        self.head = None
        self.tail.next = None
        self.tail = None






circular = CircularSLL()
print(circular.create(1))
circular.add(0,0)
circular.add(2,1)
circular.add(3,1)
circular.add(2,2)
print([node.value for node in circular ])


#print(circular.findNode(5))
#circular.iterateCSLL()
circular.remove(2)
print([node.value for node in circular ])
circular.delete()
print([node.value for node in circular ])
