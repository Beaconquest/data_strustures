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
        cq = Custom_Queue(2)
        self.assertTrue(cq.is_empty())

    def test_is_full(self):
        cq = Custom_Queue(2)
        cq.items.append('test')
        cq.items.append('test2')
        self.assertTrue(cq.is_full())

    def test_enqueue_exception(self):
        cq = Custom_Queue(1)
        cq.items.append('test')
        with self.assertRaises(Exception):
            cq.enqueue('test2')

    def test_enqueue(self):
        cq = Custom_Queue(2)
        cq.enqueue('test_enqueue')
        self.assertEqual(['test_enqueue'], ['test_enqueue'])

    def test_dequeue_exception(self):
        cq = Custom_Queue(2)
        with self.assertRaises(Exception):
            cq.dequeue()

    def test_dequeue(self):
        cq = Custom_Queue(2)
        cq.items.append('test')
        self.assertEqual(cq.dequeue(), 'test')

    def test_qsize(self):
        cq = Custom_Queue(2)
        cq.items.append('test')
        self.assertEqual(cq.qsize(), 1)

    def test_peek_exception(self):
        cq = Custom_Queue(2)
        with self.assertRaises(Exception):
            cq.peek()

    def test_peek(self):
        cq = Custom_Queue(2)
        cq.items.append('test1')
        cq.items.append('test2')
        self.assertEqual(cq.peek(), 'test1')

if __name__ == '__main__':
    unittest.main()