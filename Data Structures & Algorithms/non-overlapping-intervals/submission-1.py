class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        counter = 0

        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart < prevEnd:
                prevEnd = min(prevEnd, currEnd)
                counter += 1
            else:
                prevEnd = currEnd
        
        return counter