import unittest
from queue import *

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()

    def test_construct_works(self):
        Queue()

    def test_is_empty_with_empty_queue(self):
        self.assertTrue(self.q.is_empty())

    def test_is_empty_with_non_empty_queue(self):
        self.assertTrue(self.q.is_empty())
        self.q.enqueue(1)

        self.assertFalse(self.q.is_empty())

    def test_dequeue_with_empty_queue(self):
        self.assertTrue(self.q.is_empty())
        with self.assertRaises(Exception):
            self.q.dequeue()

    def test_dequeue_with_non_empty_queue(self):
        self.q.enqueue(77)
        self.q.enqueue(42)

        self.assertEqual(77, self.q.dequeue())
        self.assertEqual(42, self.q.dequeue())
        self.assertTrue(self.q.is_empty())


if __name__ == '__main__':
    unittest.main()