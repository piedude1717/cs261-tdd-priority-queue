# MaxHeap: A binary 'max' heap.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_max_heap.py.
# YOUR NAME

class MaxHeap:

    def __init__(self):
        self._data = []

    def _size(self):
        return len(self._data)

    def _is_empty(self):
        return len(self._data) == 0

    def _last_index(self):
        return len(self._data) - 1

    def _value_at(self, input_index):
        if 0 <= input_index <= self._size():
            return self._data[input_index]
        else:
            raise IndexError

    def _left_child_index(self, input_index):
        return (2 * input_index) + 1

    def _right_child_index(self, input_index):
        return (2 * input_index) + 2

    def _parent_index(self, input_index):
        return (input_index - 1) // 2

    def _parent(self, input_index):
        return self._value_at(self._parent_index(input_index))

    def _left_child(self, input_index):
        if self._size() < self._left_child_index(input_index):
            return None
        elif self._left_child_index(input_index) < self._size():
            return self._data[self._left_child_index(input_index)]

    def _right_child(self, input_index):
        if self._size() < self._right_child_index(input_index):
            return None
        elif self._right_child_index(input_index) < self._size():
            return self._data[self._right_child_index(input_index)]

    def _has_left_child(self, input_index):
        return self._left_child(input_index) is not None

    def _has_right_child(self, input_index):
        return self._right_child(input_index) is not None

    def _greater_child_index(self, input_index):
        if self._has_right_child(input_index) is None and self._has_left_child(input_index) is None:
            return None

        elif self._right_child(input_index) is not None and self._left_child(input_index) is not None:
            if self._left_child(input_index) < self._right_child(input_index):
                return self._right_child_index(input_index)

            else:
                return self._left_child_index(input_index)

        elif self._right_child(input_index) is None and self._left_child(input_index) is not None:
            return self._left_child_index(input_index)

    def _obeys_heap_property_at_index(self, input_index):
        if self._left_child(input_index) is None and self._right_child(input_index) is None:
            return True

        elif self._left_child(input_index) is None:
            if input_index >= self._right_child(input_index):
                return True
            else:
                return False

        elif self._right_child(input_index) is None:
            if self._data[input_index] >= self._left_child(input_index):
                return True
            else:
                return False

        elif self._data[input_index] >= self._left_child(input_index) and self._data[input_index] >= self._right_child(input_index):
            return True

    def _swap(self, first_input_index, second_input_index):
        placeHolder1 = self._data[first_input_index]
        self._data[first_input_index] = self._data[second_input_index]
        self._data[second_input_index] = placeHolder1

    def _sift_down(self, input_index):
        if self._obeys_heap_property_at_index(input_index):
            return
        greater = self._greater_child_index(input_index)
        self._swap(input_index, greater)
        return self._sift_down(greater)









