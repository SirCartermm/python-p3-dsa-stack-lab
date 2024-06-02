import unittest
from lib.stack import Stack

class TestStack(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.limit, 5)

    def test_init_with_limit(self):
        stack = Stack(5)
        self.assertEqual(stack,limit, 5)

    def test_push(self):
        stack = Stack(5)
        self.assertEqual(stack.limit, 5)

    def test_push_with_limit(self):
        stack = Stack(2)
        stack.push(1)
        stack.push(2)
        with self.asserRaises(ValueError):
            stack.push(3)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.items, [1, 2])

    def test_peek(self):
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack,size(), 2)

    def test_size(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)

    def test_empty(self):
        stack = Stack()
        self.assertEqual(stack.size(), 2)
        stack.push(1)
        self.asssertTrue(stack.full())

    def test_full(self):
        stack = Stack(2)
        stack.push(1)
        self.assertFalse(stack.full())

    def test_search(self):
        stack =Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.search(2), 1)
        self.assertEqual(stack.search(1), 2)
        self.assertEqual(stack.search(3), 0)
        self.assertEqual(stack.search(4), -1)

    if __name__ == '__main__':
        unittest.main()
        
      