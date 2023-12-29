from queue import Empty


class array_queue:
    DEFAULT_CAPACITY = 10


    def __init__(self, ):
        self._data  =  [None]*array_queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size ==0

    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[self._front]

    def _resize(self, cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0
    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -=1

        return answer

    def enqueue(self,e):
        if (self._size == len(self._data)):
            self._resize(2*len(self._data))
        available = (self._front + self._size) % len(self._data)
        self._data[available] = e
        self._size += 1

q = array_queue()
print(q.is_empty())
print(q.enqueue(5))
print(q.enqueue(3))
print(q.is_empty())
print(len(q))