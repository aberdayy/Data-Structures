# Singly Linked List
from queue import Empty

'''
We define a class called LinkedStack,
which implements a stack data structure using a singly linked list.
A stack is a collection of items that follows the last-in, first-out (LIFO) principle,
meaning that the last item added to the stack is the first one to be removed.
A singly linked list is a linear data structure that consists of nodes,
each containing an element and a reference to the next node.
The first node is called the head, and the last node is called the tail.
'''
class LinkedStack:
    '''
    The LinkedStack class has four attributes:
    _head, _size, Node, and init.
    The _head attribute stores a reference
    to the first node of the linked list, or None if the list is empty.
    The _size attribute stores the number of elements in the stack.
    '''

    def __init__(self):
        self._head =  None
        self._size = 0
    class Node:
        __slots__ = '_element', '_next'
        '''
        The Node attribute is a nested class that defines the structure of a node,
        with two slots: _element and _next.
        The init attribute is a special method that initializes a new LinkedStack object,
        setting the _head to None and the _size to 0.

        '''
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0


    def push(self, e):
        self._head = self.Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head  = self._head._next
        self._size -= 1
        return answer

'''
The LinkedStack class also has six methods: len, is_empty, push, top and pop
The len method returns the value of the _size attribute, which is the number of elements in the stack. 
The is_empty method returns True if the _size attribute is 0, or False otherwise. 
The push method adds a new element to the top of the stack, by creating a new node 
with the element and the current _head as the data and the next reference, respectively, 
and then setting the _head to the new node and incrementing the _size by 1. 
The top method returns the element of the node pointed by the _head, 
or raises an Empty exception if the stack is empty. The pop method removes and 
returns the element of the node pointed by the _head, or raises an Empty exception if the stack is empty.
It also sets the _head to the next reference of the node, and decrements the _size by 1.
'''

S = LinkedStack()

S.push(21)
S.push(431)
S.push(11)
S.push(76)
S.push(92)
print("Cikarmadan onceki top")
print(S.top())
S.pop()
print("Cikardiktan sonraki top")
print(S.top())
