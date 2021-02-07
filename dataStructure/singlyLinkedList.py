class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Add node to the list
    def insertNode(self, value, location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                nextNode = temp.next
                temp.next = newNode
                newNode.next = nextNode

    # Iterate over the list
    def traverseSinglyLinkedList(self):
        if self.head is None:
            print("Doesn't Exist!")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search value in the list
    def searchNode(self, nodeValue):
        if self.head is None:
            return "List doesn't exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "Value doesn't exist!"

    # Delete value in the list
    def removeNode(self, location):
        if self.head is None:
            print("List doesn't exist!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                nextNode = temp.next
                temp.next = nextNode.next

    # Remove entire nodes
    def removeEntireList(self):
        if self.head is None:
            print("List doesn't exist!")
        else:
            self.head = None
            self.tail = None

singlyLL = SLList()
singlyLL.insertNode(1,1)
singlyLL.insertNode(2,1)
singlyLL.insertNode(3,1)
singlyLL.insertNode(4,1)
singlyLL.insertNode(5,1)
singlyLL.insertNode(0,0)
singlyLL.insertNode(0,4)
print([node.value for node in singlyLL])
singlyLL.removeNode(3)
print([node.value for node in singlyLL])
singlyLL.removeEntireList()
print([node.value for node in singlyLL])



#singlyLL.traverseSinglyLinkedList()
#print(singlyLL.searchNode(41))



        