class DynamicArray:
    
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._arr = [None] * capacity
        self._idx = 0

    def get(self, i: int) -> int:
        if i < self._capacity:
            return self._arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self._capacity:
            self._arr[i] = n
        self._idx = max(i + 1, self._idx)

    def pushback(self, n: int) -> None:
        if self._idx == self._capacity:
            self.resize()
        self._arr[self._idx] = n
        self._idx += 1

    def popback(self) -> int:
        res = self._arr[self._idx - 1]
        self._idx -= 1
        return res 

    def resize(self) -> None:
        tmp = self._arr + [None] * self._capacity
        self._arr = tmp
        self._capacity *= 2

    def getSize(self) -> int:
        return self._idx
    
    def getCapacity(self) -> int:
        return self._capacity
