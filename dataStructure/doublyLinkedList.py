class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Create doubly linked list
    def create(self, nodeVal):
        node = Node(nodeVal)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "Successfully created!"

    # Add node to the list
    def addNode(self, nodeVal, loc):
        if self.head is None:
            print("Failed!")
        else:
            newNode = Node(nodeVal)
            if loc == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif loc == 1:
                newNode.next = None
                newNode.prev = self.tail
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

    # Iterate over the list
    def iterateDLL(self):
        if self.head is None:
            print("No element to iterate")
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next

    # Reverse the node in the list
    def reverseNode(self):
        if self.head is None:
            print("No element to reverse")
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                temp = temp.prev

    # Find node in the list
    def findNode(self, nodeVal):
        if self.head is None:
            return "No element in the list"
        else:
            temp = self.head
            while temp:
                if temp.value == nodeVal:
                    return temp.value
                temp = temp.next
            return "Node doesn't exist in the list"

    # Remove node from the list
    def removeNode(self, loc):
        if self.head is None:
            print("No element in the list")
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif loc == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                current = self.head
                idx = 0
                while idx < loc-1:
                    current = current.next
                    idx += 1
                current.next = current.next.next
                current.next.prev = current
            print(" NODE HAS BEEN DELETED!")

    # Remove the list
    def removeList(self):
        if self.head is None:
            print("No node in the list!")
        else:
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
            print("THE LIST HAS BEEN DELETED!")




doublyLL = DoublyLinkedList()
doublyLL.create(5)
print([node.value for node in doublyLL])

doublyLL.addNode(0,0)
doublyLL.addNode(2,1)
doublyLL.addNode(4,2)
doublyLL.addNode(6,2)

print([node.value for node in doublyLL])
# doublyLL.iterateDLL()
# print([node.value for node in doublyLL])
# doublyLL.reverseNode()
# print(doublyLL.findNode(6))
# print(doublyLL.findNode(8))
#doublyLL.removeNode(-1)
doublyLL.removeList()
print([node.value for node in doublyLL])



