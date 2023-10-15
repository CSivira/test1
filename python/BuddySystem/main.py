import math
import sys


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

    left = coalesce(node.left)
    right = coalesce(node.right)
    if left is None and right is None and is_free(node):
        node.left = None
        node.right = None
        return None

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
        if is_free(node.left) and is_free(node.right):
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


def show_memory_tree(node: Node, lvl: int) -> None:
    if node is not None:
        show_memory_tree(node.left, lvl + 1)
        node.show('■', lvl * 16)
        show_memory_tree(node.right, lvl + 1)


def show_memory(node: Node) -> None:
    if node is not None:
        show_memory(node.left)
        show_memory(node.right)
        if (node.left is None and node.right is None) or node.name is not None:
            node.show()


class Memory:
    def __init__(self, size: int):
        self.size = size
        self.tree = Node(size)
        self.names = []

    def reserve(self, name: str, size: int) -> None:
        if name in self.names:
            print(f"El nombre '{name}' ya fue registrado en memoria")
            return

        node = traverse(self.tree, size)
        if node is None:
            print(f"No hay suficiente espacio para reservar el nombre {name}")
        else:
            node.name = name
            self.names.append(name)

    def free(self, name: str) -> None:
        node = search(self.tree, name, None)

        if node is None:
            print(f"El nombre '{name}' no se encuentra registrado en la memoria")
            return

        if node.left is not None and node.left.name == name:
            node.left.name = None

        if node.right is not None and node.right.name == name:
            node.right.name = None

        coalesce(self.tree)

    def show(self) -> None:
        show_memory(self.tree)
        show_memory_tree(self.tree, 0)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def main():
    # memory.reserve('A', 32)
    # memory.show()
    # memory.reserve('B', 64)
    # memory.show()
    # memory.reserve('C', 60)
    # memory.show()
    # memory.reserve('D', 150)
    # memory.show()
    # memory.free('B')
    # memory.show()
    # memory.free('A')
    # memory.show()
    # memory.reserve('E', 100)
    # memory.show()
    # memory.reserve('F', 100)
    # memory.show()

    # memory.reserve("A", 256)
    # memory.show()
    # memory.reserve("C", 512)
    # memory.show()
    # memory.reserve("B", 256)
    # memory.show()
    # memory.reserve("F", 32)
    # memory.show()

    if len(sys.argv) != 2 and 0 >= int(sys.argv[1]):
        print("La cantidad de memoria no es correcto o no fue suministrada")
        return

    memory = Memory(int(sys.argv[1]))
    while True:
        command = input()

        if len(command) == 0:
            continue

        command = command.split(" ")

        match command[0]:
            case "RESERVAR":
                if len(command) != 3:
                    print("Instruccion desconocida")
                    continue

                if 0 >= int(command[1]) or int(command[1]) > int(sys.argv[1]):
                    print("La cantidad de memoria solicitada no es valida")
                    continue

                memory.reserve(command[2], int(command[1]))
            case "LIBERAR":
                if len(command) != 2:
                    print("Instruccion desconocida")
                    continue

                memory.free(command[1])

            case "MOSTRAR":
                memory.show()

            case "SALIR":
                break

            case _:
                print("Instruccion desconocida")


if __name__ == "__main__":
    main()
