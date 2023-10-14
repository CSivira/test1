import math

from python.BuddySystem.Node import Node


def split(node: Node) -> int:
    return 2 ** math.floor(math.log(node.size, 2)) / 2


def free(node: Node, name: str) -> Node | None:
    if node is None:
        return None

    if node.name == name:
        node.name = None
        return node

    result_l = free(node.left, name)
    if result_l is not None:
        if node.right.name is None:
            node.parent.parent = None
            return None

    result_r = free(node.right, name)
    if result_r is not None:
        if node.left.name is None:
            node.parent.parent = None
            return None


def reserve(node: Node, blocks: int, name: str) -> Node | None:
    if node.size < blocks:
        return None

    split_size = split(node)
    if split_size < blocks and node.name is None:
        # aca se puede agregar a una estructura adicional para rapido acceso
        node.name = name
        node.used = blocks
        node.free = node.size - blocks

        # if node.parent is not None:
        #    node.parent.size = node.parent.size - node.size

        return node

    if node.left is None:
        node.left = Node(split_size, node)

    if node.right is None:
        node.right = Node(node.size - split_size, node)

    if node.left.name is None:
        result = reserve(node.left, blocks, name)
        if result is not None:
            return result

    if node.right.name is None:
        result = reserve(node.right, blocks, name)
        if result is not None:
            return result


def traverseTree(node: Node, level: int) -> None:
    tab_size = 8
    if node is None:
        return

    node_name = node.name if node.name is not None else "~"

    traverseTree(node.left, level + 1 if level != 0 else 0)
    print("|", "-" * level * tab_size, "|", node.size, "|", node_name)
    traverseTree(node.right, level + 1 if level != 0 else 0)


def traverseTable(node: Node, addr: int) -> None:
    row_size = 32

    if node is None:
        return

    split_size = split(node)
    traverseTable(node.left, split_size)
    traverseTable(node.right, addr + node.size)
    if node.name is not None or (node.left is None and node.right is None):
        used_percentage = int((node.used / node.size) * row_size)
        free_percentage = int((node.free / node.size) * row_size)
        node_name = node.name if node.name is not None else "~"
        print("|", node.size, "|", node_name, "|", '■' * used_percentage + '□' * free_percentage)



class Memory:
    def __init__(self, blocks: int):
        self.blocks = blocks
        self.used_blocks = 0
        self.tree = Node(blocks, None, '')
        self.tree.free = self.tree.size

    def reserve(self, blocks: int, name: str):
        reserve(self.tree, blocks, name)
        self.used_blocks = self.used_blocks + blocks

    def free(self, name):
        free(self.tree, name)

    def show(self):
        traverseTable(self.tree, 0)
        traverseTree(self.tree, 1)
