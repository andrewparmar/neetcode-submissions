class DynamicArray:
    
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._length = 0
        self._arr = [0] * capacity

    def get(self, i: int) -> int:
        return self._arr[i]

    def set(self, i: int, n: int) -> None:
        self._arr[i] = n 

    # TBD
    def pushback(self, n: int) -> None:
        if self._length >= self._capacity:
            self.resize()
        self._arr[self._length] = n
        self._length += 1

    def popback(self) -> int:
        self._length -= 1
        return self._arr[self._length]

    def resize(self) -> None:
        self._arr = self._arr + [0] * self._capacity
        self._capacity *= 2

    def getSize(self) -> int:
        return self._length
    
    def getCapacity(self) -> int:
        return self._capacity
