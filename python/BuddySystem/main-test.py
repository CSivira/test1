import unittest
from main import Node, Memory, is_free, coalesce, search, traverse


class TestMemoryMethods(unittest.TestCase):
    def setUp(self):
        self.memory = Memory(100)
        self.parent = Node(50)
        self.node = Node(50)

    def test_is_free(self):
        self.assertTrue(is_free(self.node))
        self.node.name = "test"
        self.assertFalse(is_free(self.node))

    def test_traverse(self):
        self.assertIsNone(traverse(None, 10))
        self.assertIsNotNone(traverse(self.memory.tree, 50))
        self.assertIsNotNone(traverse(self.memory.tree, 100))

    def test_search(self):
        self.assertIsNone(search(self.node, "test", None))

        self.node.name = "test"
        self.assertIsNotNone(search(self.node, "test", self.parent))

        self.node.name = None
        self.node.left = Node(50)
        self.node.left.name = "test-left"
        self.assertIsNotNone(search(self.node, "test-left", self.parent))

        self.node.name = None
        self.node.right = Node(50)
        self.node.right.name = "test-right"
        self.assertIsNotNone(search(self.node, "test-right", self.parent))

    def test_coalesce(self):
        self.assertIsNone(coalesce(None))

        self.node.left = Node(25)
        self.node.right = Node(25)
        self.assertIsNone(coalesce(None))

        self.node.left = Node(25)
        self.node.left.name = "A"
        self.node.right = Node(25)
        self.assertIsNotNone(coalesce(self.node))

        self.node.left = Node(25)
        self.node.right = Node(25)
        self.node.right.name = "A"
        self.assertIsNotNone(coalesce(self.node))

        self.node.left = Node(25)
        self.node.left.name = "B"
        self.node.right = Node(25)
        self.node.right.name = "A"
        self.assertIsNotNone(coalesce(self.node))


if __name__ == '__main__':
    unittest.main()
