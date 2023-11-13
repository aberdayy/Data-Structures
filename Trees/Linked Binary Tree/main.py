class Tree:

    class Position:
        def element(self):
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            raise NotImplementedError('Must be implemented by subclass')

    def root(self):
        raise NotImplementedError('Must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('Must be implemented by subclass')

    def is_root(self, param):
        return self.root() == param

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p): # from surface
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    # def _height1(self):
    #   return max(self.depth(p) for p in self.positions() if self.is_leaf())

    def _height2(self, p): # from ground
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
        if p is None:
            p = self.root()
        return self._height2(p)

class BinaryTree(Tree):

    def left(self,  p):
        raise NotImplementedError('Must be implemented by subclass')

    def root(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)

        if parent is None:
            return None
        else:
            if p == self.left(parent):
                self.right(parent)
            else:
                p == self.right(parent)
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

class LinkedBinaryTree(BinaryTree):
    class Node:
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def _validate(self,p):
            if not isinstance(p, self.Position):
                raise TypeError(f'{p} must be a proper positon type')
            if p._container is not self:
                raise ValueError(f'{p} does not belong to this container')
            if p._node._parent is p._node:
                raise ValueError(f'{p} is no longer valid')
            return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self,  p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def add_root(self, e):
        if self.root is not None:
            raise ValueError(f'{e} root already exists')
        self._size = 1
        self._root = self.Node(e)
        return self._make_position(self._root)

    def add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('left child already exists')
        self._size += 1
        node._left = self.Node(e, node)
        return self._make_position(node._left)

    def add_right (self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('right child already exists')
        self._size += 1
        node._right = self.Node(e, node)
        return self._make_position(node._right)

    def replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self,p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError(f'{p}  has 2 children')
        child  = node._left if node._left else node._right
        if child is not None:
            child._parent  = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be a leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError("tree types must be the same")
        self._size += len(t1) + len(t2)

        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            t2._root._parent = node
            node._left = t2._root
            t2._root = None
            t2._size = 0
