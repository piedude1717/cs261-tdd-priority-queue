# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# abhimanyu, bais

class NaivePriorityQueue:

    def __init__(self):
        self.data = []

    def enqueue(self, item):
        return self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        highest_priority = 0
        victim = 0
        while victim < len(self.data):
            if self.data[highest_priority] < self.data[victim]:
                highest_priority = victim
            victim += 1
        return self.data.pop(highest_priority)

    def is_empty(self):
        return len(self.data) == 0

