class MinStack:

    def __init__(self):
        self.stack = []
        self._min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self._min:
            self._min.append(val)
        else:
            if val <= self._min[-1]:
                self._min.append(val)

    def pop(self) -> None:
        item = self.stack.pop()        
        if self._min[-1] == item:
            self._min.pop()

    def top(self) -> int:
       return self.stack[-1] 

    def getMin(self) -> int:
        if self._min:
            return self._min[-1]
