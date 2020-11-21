# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# YOUR NAME

class NaivePriorityQueue:

    def __init__(self, data=None):
        self.data = []
        self.data.append(data)

    def enqueue(self, item):
        return self.data.append(item)

    def dequeue(self):
        return self.data.pop()
