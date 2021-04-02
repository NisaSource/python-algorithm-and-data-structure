class Heap:
    def __init__(self, sz):
        self.list = (sz + 1) * [None]
        self.heapSz = 0
        self.maxSz = sz + 1


def heap_peek(root):
    if not root:
        return
    else:
        return root.list[1]


def heap_size(root):
    if not root:
        return
    else:
        return root.heapSz


def level_order_traversal(root):
    if not root:
        return
    else:
        for i in range(1, root.heapSz+1):
            print(root.list[i])


def insert_heap_tree(root, idx, type):
    parent_idx = int(idx/2)
    if idx <= 1:
        return
    if type == "Min":
        if root.list[idx] < root.list[parent_idx]:
            temp = root.list[idx]
            root.list[idx] = root.list[parent_idx]
            root.list[parent_idx] = temp
        insert_heap_tree(root, parent_idx, type)
    elif type == "Max":
        if root.list[idx] > root.list[parent_idx]:
            temp = root.list[idx]
            root.list[idx] = root.list[parent_idx]
            root.list[parent_idx] = temp
        insert_heap_tree(root, parent_idx, type)


def insert_node(root, val, type):
    if root.heapSz + 1 == root.maxSz:
        return "FULL"
    root.list[root.heapSz + 1] = val
    root.heapSz += 1
    insert_heap_tree(root, root.heapSz, type)
    return "SUCCESSFULLY INSERTED"


new_binary_heap = Heap(5)
insert_node(new_binary_heap, 6, "Max")
insert_node(new_binary_heap, 7, "Max")
insert_node(new_binary_heap, 5, "Max")
insert_node(new_binary_heap, 4, "Max")
level_order_traversal(new_binary_heap)
