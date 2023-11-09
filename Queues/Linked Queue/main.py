#Linked Queue List
from queue import Empty


class LinkedQueue:
    class Node:
            __slots__ = '_element', '_next'
            def __init__(self, element, next):
                self._element = element
                self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Linked queue is empty')
        return self._head._element

    def dequeue(self):
        if (self.is_empty()):
            raise Empty('Linked queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -=1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self,e):
        newest = self.Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1



L = LinkedQueue()
L.enqueue(22)
L.enqueue(51)
L.enqueue(90099)
print("asagidaki toplam eleman sayisi")
print(L.__len__())
print("asagidaki ilk eleman")
print(L.first())
print("asagidaki cikarildi")
print(L.dequeue())
print("asagidaki yeni ilk eleman")
print(L.first())
print("asagidaki toplam eleman sayisi")
print(L.__len__())