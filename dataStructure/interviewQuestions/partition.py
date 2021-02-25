# Write code to partition a linked list around n value,
# such that all nodes less than x come before all nodes greater than or equal to n.

from LinkedList import LinkedList

def partition(list, n):
    current = list.head
    list.tail = list.head

    while current:
        nextNode = current.next
        current.next = None
        if current.value < n:
            current.next = list.head
            list.head = current
        else:
            list.tail.next = current
            list.tail = current
        current = nextNode

    if list.tail.next is not None:
        list.tail.next = None


linkedList = LinkedList()
linkedList.generate(10, 0, 100)
print(linkedList)
partition(linkedList, 60)
print(linkedList)
