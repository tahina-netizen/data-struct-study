"""
A LIFO data strucuture.
"""
class Stack:
    """
    Create an empty stack
    """
    def __init__(self):
        self._content = []

    """
    Tell if this stack is empty
    :return: (bool) True iff this stack is empty
    """
    def is_empty(self):
        return self._content == []

    """
    Push x on this stack
    :param x: element to be pushed in this stack
    """
    def push(self, x):
        self._content.append(x)

    """
    Gives the last inserted element, if this stack is not empty.
    If this stack is empty, an exception is raised.
    :return: (any) the last inserted element (if this stack is not empty)
    """
    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack: trying to pop from it")
        return self._content.pop(len(self._content) - 1)