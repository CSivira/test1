class Node:

    def __init__(self,
                 size: int = 0,
                 parent: 'Node' = None,
                 name: str = None,
                 left: 'Node' = None,
                 right: 'Node' = None):
        self.size = int(size)
        self.parent = parent
        self.name = name
        self.left = left
        self.right = right
        self.used = 0
        self.free = size

    def print(self) -> None:
        print(self.size, self.name, self.parent.size if self.parent is not None else None, self.used, self.free)
