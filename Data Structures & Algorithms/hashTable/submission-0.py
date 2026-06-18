class Pair:
    def __init__(self, k, v):
        self.key = k
        self.val = v

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * capacity

    def hash(self, key: int):
        idx = key % self.capacity
        return idx

    def get(self, key: int) -> int:
        idx = self.hash(key)
        while self.table[idx] is not None:
            if self.table[idx].key == key:
                return self.table[idx].val
            else:
                idx = (idx + 1) % self.capacity
        return -1
            
    def insert(self, key: int, value: int) -> None:
        idx = self.hash(key)
        count = 0
        while self.table[idx] is not None and count < self.capacity:
            if self.table[idx].key == key:
                self.table[idx].val = value
                return
            else:
                idx = (idx + 1) % self.capacity
            count += 1
        self.table[idx] = Pair(key, value)
        self.resize()

    def remove(self, key: int) -> bool:
        idx = self.hash(key)
        count = 0
        while self.table[idx] is not None and count < self.capacity:
            if self.table[idx].key == key:
                self.table[idx] = None
                return True
            else:
                idx = (idx + 1) % self.capacity
            count += 1
        return False

    def getSize(self) -> int:
        res = 0
        for x in self.table:
            if x is not None:
                res += 1
        return res

    def getCapacity(self) -> int:
        print(self.capacity)
        return self.capacity

    def resize(self) -> None:
        if self.getSize() < self.capacity//2:
            return
        tmp = [None] * self.capacity * 2
        new_cap = len(tmp)
        for x in self.table:
            if x:
                # compute new hash
                idx = x.key % new_cap

                # insert into table
                while tmp[idx] is not None:
                    idx = (idx + 1) % new_cap
                tmp[idx] = x
        self.table = tmp
        self.capacity = len(tmp)
