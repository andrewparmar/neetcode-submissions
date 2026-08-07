from heapq import heapify, heapify_max, heappush, heappop, heappush_max, heappop_max
import heapq as hq

class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []
        hq.heapify_max(self.lo)
        hq.heapify(self.hi)

    def addNum(self, num: int) -> None:
        if len(self.lo) == len(self.hi):
            hq.heappush_max(self.lo, hq.heappushpop(self.hi, num))
        else:
            hq.heappush(self.hi, hq.heappushpop_max(self.lo, num))

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (self.lo[0] + self.hi[0]) / 2
        else:
            return self.lo[0]
        
        