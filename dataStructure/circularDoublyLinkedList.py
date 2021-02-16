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

   
circularDLL = CircularDoublyLL()


print([node.value for node in circularDLL])