
# from .. import LinkedList
from dataStructure.LinkedList import LinkedList


def nthToLastEl(list, n):
    p1 = list.head
    p2 = list.head

    for i in range(n):
        if p2 is None:
            return None
        p2 = p2.next
    
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1

linkedList = LinkedList()
linkedList.generate(10, 0, 100)
print(linkedList)

print(nthToLastEl(linkedList, 6))
