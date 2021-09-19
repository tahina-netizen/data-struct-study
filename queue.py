"""
A FIFO data structure.
"""
class Queue:
    
    """
    Create an empty queue
    """
    def __init__(self):
        self._content = []

    """
    Tell if this queue is empty
    :return: (bool) True iff this queue is empty
    """
    def is_empty(self):
        return self._content == []

    """
    Enqueue x on this queue
    """
    def enqueue(self, x):
        self._content.append(x)

    """
    Dequeue this queue if it's not empty.
    If this queue is empty, an exception is raised.

    :return: (any) the dequeued element of this queue
    """
    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty queue: trying to dequeue from it")
        
        return self._content.pop(0)