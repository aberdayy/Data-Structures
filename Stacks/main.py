# Array Stacks
from queue import Empty


class array_stack:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if len(self._data)==0:
            return True
        return False

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty!')
        else:
            return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty!')
        else:
            self._data.pop()

ourStack = array_stack()

print(ourStack.__len__())
ourStack.push('a')
ourStack.push(7)
ourStack.push('dasdasd')
ourStack.push('33')
print(ourStack.top())
print(ourStack.pop())
print(len(ourStack))

