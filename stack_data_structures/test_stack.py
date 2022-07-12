import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    """ Test the Stack class from the module stack.py. """
    
    def test_push(self):
        s = Stack()
        s.push("test")
        self.assertEqual(["test"], ["test"])
    
    def test_pop(self):
        s = Stack()
        s.stack.append('test')
        self.assertEqual(s.pop(), 'test')
    
    def test_pop_exception(self):
        s = Stack()
        with self.assertRaises(Exception):
            s.pop()

    def test_peek(self):
        s = Stack()
        s.stack.append('test')
        self.assertEqual(s.peek(), 'test')

    def test_peek_exception(self):
        s = Stack()
        with self.assertRaises(Exception):
            s.peek()
    
    def test_is_empty_true(self):
        s = Stack()
        self.assertTrue(s.is_empty()) 
    
    def test_is_empty_false(self):
        s = Stack()
        s.stack.append('test')
        self.assertFalse(s.is_empty())

    def test_size(self):
        s = Stack()
        s.stack.append('test')
        self.assertEqual(s.size(), 1)

if __name__ == "__main__":
    unittest.main()   