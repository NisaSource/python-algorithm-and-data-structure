import QueueLinkedList as Q


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


binaryTree = Tree("Foods")
left = Tree("Salad")
caesar = Tree("Caesar")
greek = Tree("Greek")
right = Tree("Pizza")
left.left = caesar
left.right = greek
binaryTree.left = left
binaryTree.right = right


def pre_order(root):
    if not root:
        return
    print(root.data)
    pre_order(root.left)
    pre_order(root.right)


print("PRE ORDER: ROOT-LEFT-RIGHT")
print("---------------------------")
pre_order(binaryTree)
print("---------------------------")


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.data)
    in_order(root.right)


print("IN ORDER: LEFT-ROOT-RIGHT")
print("---------------------------")
in_order(binaryTree)
print("---------------------------")


def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data)


print("POST ORDER: LEFT-RIGHT-ROOT")
print("---------------------------")
post_order(binaryTree)
print("---------------------------")


def level_order(root):
    if not root:
        return
    else:
        new_q = Q.Queue()
        new_q.enqueue(root)
        while not(new_q.isEmpty()):
            r = new_q.dequeue()
            print(r.value.data)
            if r.value.left is not None:
                new_q.enqueue(r.value.left)
            if r.value.right is not None:
                new_q.enqueue(r.value.right)


print("LEVEL ORDER")
print("---------------------------")
level_order(binaryTree)
print("---------------------------")


def search_node(root, val):
    if not root:
        return "The tree doesn't exist!"
    else:
        new_q = Q.Queue()
        new_q.enqueue(root)
        while not new_q.isEmpty():
            r = new_q.dequeue()
            if r.value.data == val:
                return "FOUND!"
            if r.value.left is not None:
                new_q.enqueue(r.value.left)
            if r.value.right is not None:
                new_q.enqueue(r.value.right)
        return "THERE'S SUCH NODE IN THE TREE"


print(search_node(binaryTree, "Meat"))
print(search_node(binaryTree, "Cheese"))


def insert_node(root, new_node):
    if not root:
        root = new_node
    else:
        new_q = Q.Queue()
        new_q.enqueue(root)
        while not new_q.isEmpty():
            r = new_q.dequeue()
            if r.value.left is not None:
                new_q.enqueue(r.value.left)
            else:
                r.value.left = new_node
                return "Successfully inserted"
            if r.value.right is not None:
                new_q.enqueue(r.value.right)
            else:
                r.value.right = new_node
                return "Successfully inserted"


new_node = Tree("Margarita")
print(insert_node(binaryTree, new_node))
level_order(binaryTree)