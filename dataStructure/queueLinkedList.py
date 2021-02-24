from LinkedList import LinkedList
from LinkedList import Node

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    
    def __str__(self):
        values = [str(val) for val in self.linkedList]
        return " ".join(values)

    # Check if the queue is empty
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    # Add element to the queue
    def enqueue(self, val):
        newNode = Node(val)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    # Remove element from the queue
    def dequeue(self):
        if self.isEmpty():
            return "The Queue is EMPTY"
        else:
            temp = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return temp

    # Check and return the first element in the queue
    def peek(self):
        if self.isEmpty():
            return "The Queue is EMPTY"
        else:
            return self.linkedList.head

    # Delete entire queue
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None



queueLL = Queue()
queueLL.enqueue(1)
queueLL.enqueue(2)
queueLL.enqueue(3)
print(queueLL)
print(queueLL.dequeue())
print(queueLL)
print(queueLL.peek())
print(queueLL)
queueLL.delete()
print(queueLL)
