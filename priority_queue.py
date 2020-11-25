# PriorityQueue: An efficient priority queue.
# If you use a binary heap, it'll do most of the work, leaving this
# implementation quite trivial.
# Your implementation should pass the tests in test_priority_queue.py.
# Abhimanyu, bais

from max_heap import MaxHeap


class PriorityQueue:

    heap = MaxHeap()


class PriorityQueue:
    def __init__(self):
        self.heap = MaxHeap()
    pass

    def enqueue(self, value):
        return self.heap.insert(value)

    def dequeue(self):
        return self.heap.delete()

    def is_empty(self):
        return self.heap._is_empty()