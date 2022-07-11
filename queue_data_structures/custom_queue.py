from queue import Queue

class Custom_Queue:

    def __init__(self, maxsize=int):
        self.maxsize = maxsize
        self.items = []

    def is_empty(self):
        """ Returns True if queue is empty. """
        return len(self.items) == 0
    
    def is_full(self):
        """ Return True if there are maxsize items in the queue. """
        return self.qsize() == self.maxsize

    def enqueue(self, item):
        """ Add a new element to the end of queue. """
        if self.is_full():
            raise IndexError("Queue is full.")
        
        self.items.append(item)

    def dequeue(self):
        """ remove an element fromt he beginning of the queue. """
        if self.is_empty():
            raise IndexError('Queue is empty.')
        return self.items.pop(0)

    def qsize(self):
        """ Returns the number of items in the queue. """
        return len(self.items)

    def peek(self):
        """ Have a look at first element of the queue. """
        if self.is_empty():
            raise IndexError('Nothing to peek.')
        
        return self.items[0]

q = Custom_Queue(3)