from queue import Empty


class CircularQueue:
    class Node:
            __slots__ = '_element', '_next'

            def __init__(self, element, next):
                self._element = element
                self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Circular queue is empty')
        return self._tail._next._element

    def enqueue(self, e):
        newest = self.Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest

        self._tail = newest
        self._size += 1
        return newest

    def dequeue(self):
        if self.is_empty():
            raise Empty('Circular queue is empty')
        head = self._tail._next
        if  self._size == 1:
            self._tail = None
        self._tail._next = head._next
        self._size -= 1
        return head

    def rotate(self):
        self._tail = self._tail._next

cq = CircularQueue()
print(len(cq))
cq.is_empty()
cq.enqueue(23)
cq.enqueue(91)
cq.enqueue(544)
print("Dequeue oncesi first")
print(cq.first())
cq.dequeue()
print("Dequeue sonrasi first")
print(cq.first())
