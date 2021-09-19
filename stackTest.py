import unittest
from stack import *

class QueueTest(unittest.TestCase):

    def setUp(self):
        self.q = Stack()

    def test_construct_works(self):
        Stack()

    def test_is_empty_with_empty_stack(self):
        self.assertTrue(self.q.is_empty())

    def test_is_empty_with_non_empty_stack(self):
        self.assertTrue(self.q.is_empty())
        self.q.push(1)

        self.assertFalse(self.q.is_empty())

    def test_pop_with_empty_stack(self):
        self.assertTrue(self.q.is_empty())
        with self.assertRaises(Exception):
            self.q.pop()

    def test_dequeue_with_non_empty_stack(self):
        self.q.push(77)
        self.q.push(42)

        self.assertEqual(42, self.q.pop())
        self.assertEqual(77, self.q.pop())
        self.assertTrue(self.q.is_empty())


if __name__ == '__main__':
    unittest.main()