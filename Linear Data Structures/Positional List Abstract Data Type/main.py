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


class positionalList(DoublyLinkedBase):

    class Position:
        def __init__(self, container,node):
            self._container = container
            self._node  =  node

        def element(self):
            return self._node._element

        def __eq__(self, other): # check equality (==)
            return type(other) is type(self)  and other._node is self._node

        def __ne___(self,other): # check non equality (!=)
            return not(self==other)

     # utiliy
    def _validate(self,param):
        if not isinstance(param, self.Position):
            raise TypeError(f'{param} must be proper Position type')
        if param._container is not self:
            raise ValueError(f'{param} does not belont to this container')
        if param._node._next is None:
            raise ValueError(f'{param} is no longer valid')
        return param._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self,p):
        node =  self._validate(p)
        return self._make_position(node._prev)

    def after (self,p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor =  self.first()
        while cursor is not  None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)
    def add_first(self, e):
        node = self._insert_between(e,self._header,self._header._next)
        return self._make_position(node)
    def add_last(self,e):
        node = self._insert_between(e,self._trailer._prev, self._trailer)
        return self._make_position(node)
    def  add_before(self, p,  e):
        original =  self._validate(p)
        return self._insert_between(e,original._prev, original)

    def delete(self,p):
        original = self._validate(p)
        self._delete_node(original)

    def replace(self,p,e):
        original = self._validate(p)
        oldVal = original._element
        original._element  = e
        return oldVal

