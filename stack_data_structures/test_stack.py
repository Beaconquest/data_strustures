import unittest
from stack import Stack

# test_is_empty_true
s = Stack()

# test_is_empty_false and test_push data 
s1 = Stack()
s1.push('test')

# test_is_empty_false dat 
s2 = Stack()
s2.push('test')


class TestStack(unittest.TestCase):
    """ Test the Stack class from the module stack.py. """
    
    def test_push(self):
        s1.push("test2")
        self.assertEqual(["test", "test2"], ["test", "test2"])
    
    def test_pop(self):
        self.assertEqual(s2.pop(), 'test')
    
    def test_pop_exception(self):
        with self.assertRaises(Exception):
            s.pop()

    def test_peek(self):
        self.assertEqual(s1.peek(), 'test')

    def test_peek_exception(self):
        with self.assertRaises(Exception):
            s.peek()
    
    def test_is_empty_true(self):
        self.assertTrue(s.is_empty()) 
  
    def test_is_empty_false(self):
        self.assertFalse(s1.is_empty())

    def test_size(self):
        self.assertEqual(s.size(), 0)

if __name__ == "__main__":
    unittest.main()   