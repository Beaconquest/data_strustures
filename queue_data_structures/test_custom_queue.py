import unittest

from custom_queue import Custom_Queue

# Test data
cq = Custom_Queue(4)

cq1 = Custom_Queue(1)
cq1.enqueue('Test')

cq2 = Custom_Queue(1)

cq3 = Custom_Queue(3)

cq3.enqueue('dequeue_test')
cq3.enqueue('peek_test')

class TestCustom_Queue(unittest.TestCase):
    """ UnitTest for the Custom_Queue class from the custom_queue module. """

    def test_is_empty(self):
        self.assertTrue(cq.is_empty())

    def test_is_full(self):
        self.assertTrue(cq1.is_full())

    def test_enqueue_exception(self):
        with self.assertRaises(Exception):
            cq1.enqueue('test2')

    def test_enqueue(self):
        cq2.enqueue('test_enqueue')
        self.assertEqual(['test_enqueue'], ['test_enqueue'])

    def test_dequeue_exception(self):
        with self.assertRaises(Exception):
            cq2.dequeue()

    def test_dequeue(self):
        self.assertEqual(cq3.dequeue(), 'dequeue_test')

    def test_qsize(self):
        self.assertEqual(cq1.qsize(), 1)

    def test_peek_exception(self):
        with self.assertRaises(Exception):
            cq.peek()

    def test_peek(self):
        self.assertEqual(cq3.peek(), 'peek_test')

if __name__ == '__main__':
    unittest.main()