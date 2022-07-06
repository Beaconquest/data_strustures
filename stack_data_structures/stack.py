# Creating a list to be used a stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        """ Add an element to the stack. """
        self.stack.append(data)

    def pop(self):
        """ remove the top element of the stack. """
        if self.is_empty():
            raise Exception('Nothing to pop.')

        return self.stack.pop(len(self.stack) - 1)

    def peek(self):
        """ Have a look at top element of the stack. """
        if self.is_empty():
            raise Exception('Nothing to peek')

        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        """ Returns true if stack is empty. """
        if self.size() == 0:
            return True
        
        return False

    def size(self):
        """ Returns size fo the stack. """
        return len(self.stack)
    
    def __repr__(self):
        return f"Stack()"

    def __str__(self):
        return f"{self.stack}"
