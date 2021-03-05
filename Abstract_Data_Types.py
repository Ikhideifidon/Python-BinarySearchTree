class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


# Stack
class ArrayStack:
    """LIFO stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []  # Nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty."""
        if len(self._data) == 0:
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """Remove and return the element at the top of the stack.

        Raise Empty exception if the stack is empty."""
        if len(self._data) == 0:
            raise Empty("Stack is empty")
        return self._data.pop()


if __name__ == "__main__":
    s = ArrayStack()
    A = [8, 1, 5, 21, 2, 7]
    for i in A:
        s.push(i)
    print(len(s))
    print("\n")
    print(s.pop())
    print(s.top())
    for i in range(len(s)):
        print(s.pop())


# Queue
class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if queue is empty: False otherwise."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the first element at the front of the queue.

        If empty, raise an exception."""

        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO)."""
        if self.is_empty():
            raise Empty("Queue is empty")

        answer = self._data[self._front]
        self._data[self._front] = None  # Help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # Keep track of the existing list
        self._data = [None] * cap  # Allocate list with new capacity
        for k in range(self._size):  # Only consider existing elements
            self._data[k] = old[self._front]
            self._front = (self._front + 1) % len(self._data)
        self._front = 0  # Front has been realigned


if __name__ == "__main__":
    Q = ArrayQueue()
    A = [8, 1, 5, 21, 2, 7, 4, 22, 3, 18, 6]
    for i in A:
        Q.enqueue(i)

    print(Q.dequeue())
    print(Q.first())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
