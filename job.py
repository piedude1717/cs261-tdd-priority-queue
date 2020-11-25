# Job: A process or task that has a priority.
# Your implementation should pass the tests in test_job.py.
# Abhimanyu, bais

class Job:

    def __init__(self, priority=None, message=None):
        self.priority = priority
        self.message = message

    def __eq__(self, other):
        return self.priority is other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __repr__(self):
        return "Job " + str(self.priority) + ': ' + str(self.message)
