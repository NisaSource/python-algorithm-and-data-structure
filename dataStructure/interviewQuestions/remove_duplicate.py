from LinkedList import LinkedList

def removeDuplicate(list):
    if list.head is None:
        return "List doesn't exist!"
    else:
        current = list.head
        temp = set([current.value])
        while current.next:
            if current.next.value in temp:
                current.next = current.next.next
            else:
                temp.add(current.next.value)
                current = current.next
        return list


linkedList = LinkedList()
linkedList.generate(10, 10, 100)
print(linkedList)
removeDuplicate(linkedList)
print(linkedList)
