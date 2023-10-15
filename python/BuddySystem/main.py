import math


def split(size: int) -> int:
    return 2 ** math.floor(math.log(size, 2))


class Node:
    def __init__(self, _size: int):
        self.size = _size
        self.name = None
        self.left = None
        self.right = None

    def show(self, lvl: str = '', size: int = 0) -> None:
        print(lvl * size, f"({self.name}, {self.size})")


def is_free(node: Node) -> bool:
    if node is None:
        return True

    if node.name is not None:
        return False

    return is_free(node.left) and is_free(node.right)


def coalesce(node: Node) -> Node | None:
    if node is None:
        return None

    if node.left is not None and node.right is not None:
        if is_free(node.left) and is_free(node.right) is None:
            return None

    node.left = coalesce(node.left)
    node.right = coalesce(node.right)
    
    return node


def search(node: Node, name: str, parent: Node | None) -> Node | None:
    if node is None:
        return

    if node.name == name:
        return parent

    return search(node.left, name, node) or search(node.right, name, node)


def traverse(node: Node, size: int) -> Node | None:
    if node is None:
        return None

    split_size = split(node.size) // 2
    if node.size == size or size > split_size:
        available_space = node.size

        if node.left is not None and node.left.name is not None:
            available_space = available_space - node.left.size

        if node.right is not None and node.right.name is not None:
            available_space = available_space - node.right.size

        if available_space >= size:
            return node
        else:
            return None

    if node.left is None:
        node.left = Node(split_size)

    if node.right is None:
        node.right = Node(split_size)

    if node.left.name is None:
        left = traverse(node.left, size)
        if left is not None and left.name is None:
            return left

    if node.right.name is None:
        right = traverse(node.right, size)
        if right is not None and right.name is None:
            return right


def traverse_tree(node: Node, lvl: int) -> None:
    if node is not None:
        traverse_tree(node.left, lvl + 1)
        node.show('■', lvl * 16)
        traverse_tree(node.right, lvl + 1)


def traverse_memory(node: Node) -> None:
    if node is not None:
        traverse_memory(node.left)
        traverse_memory(node.right)
        if (node.left is None and node.right is None) or node.name is not None:
            node.show()


class Memory:
    def __init__(self, size: int):
        self.size = size
        self.tree = Node(size)

    def reserve(self, name: str, size: int) -> None:
        node = traverse(self.tree, size)

        if node is None:
            print("No")
        else:
            node.name = name

    def free(self, name: str) -> None:
        node = search(self.tree, name, None)

        if node.left is not None and node.left.name == name:
            node.left.name = None

        if node.right is not None and node.right.name == name:
            node.right.name = None

        coalesce(self.tree)

    def show(self) -> None:
        traverse_memory(self.tree)
        traverse_tree(self.tree, 0)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def main():
    memory = Memory(1024)

    memory.reserve('A', 32)
    memory.show()
    memory.reserve('B', 64)
    memory.show()
    memory.reserve('C', 60)
    memory.show()
    memory.reserve('D', 150)
    memory.show()
    memory.free('B')
    memory.show()
    memory.free('A')
    memory.show()
    memory.reserve('E', 100)
    memory.show()
    memory.reserve('F', 100)
    memory.show()

    # memory.reserve("A", 256)
    # memory.show()
    # memory.reserve("C", 512)
    # memory.show()
    # memory.reserve("B", 256)
    # memory.show()
    # memory.reserve("F", 32)
    # memory.show()


if __name__ == "__main__":
    main()
