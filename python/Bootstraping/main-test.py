import unittest
from main import is_compilable


class TestIsCompilable(unittest.TestCase):
    def setUp(self):
        self.interpreters = {"Python": "LOCAL", "Java": "Python"}
        self.translators = {"Python": {"JavaScript": "Java"}}

    def test_is_compilable_local(self):
        self.assertTrue(is_compilable("LOCAL", self.interpreters, self.translators))

    def test_is_compilable_interpreter(self):
        self.assertTrue(is_compilable("Python", self.interpreters, self.translators))

    def test_is_compilable_translator(self):
        self.assertTrue(is_compilable("JavaScript", self.interpreters, self.translators))

    def test_is_not_compilable(self):
        self.assertFalse(is_compilable("C++", self.interpreters, self.translators))


if __name__ == '__main__':
    unittest.main()
