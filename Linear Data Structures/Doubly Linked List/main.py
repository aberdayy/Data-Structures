# Doubly Linked
from queue import Empty


class DoublyLinkedBase:

    class Node:
        def  __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._header = self.Node(None,None,None)
        self._trailer = self.Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self.Node(e, predecessor,successor )
        predecessor._next = newest
        successor._prev = newest
        self._size +=1
        return newest

    def _delete_node(self,node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -=1
        deleted_element = node._element

        node._prev = node._next = node._element = None
        '''
        node._prev = None
        node._next = None
        node._element = None
        '''
        return deleted_element

class LinkedDoubleEndedQueue(DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next
    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev

    def insert_first(self, e):
        self._insert_between(e,self._header,self._header._next)

    def insert_last(self,e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        self._delete_node(self._trailer._prev)


ld = LinkedDoubleEndedQueue()
ld.insert_first("Edirne")
ld.insert_last("Kars")
ld._insert_between("Ankara",ld.first(),ld.last())
print(ld.__len__())
