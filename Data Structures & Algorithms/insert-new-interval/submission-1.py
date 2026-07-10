class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        ----          ---- ----
             --------
        """
        newStart, newEnd = newInterval
        res = []
        for i in range(len(intervals)):
            currStart, currEnd = intervals[i]
            if newStart <= currStart <= newEnd or currStart <= newStart <= currEnd:
                newStart, newEnd = min(currStart, newStart), max(currEnd, newEnd)
                continue
            if currEnd < newStart:
                res.append(intervals[i])
            if newEnd < currStart:
                res.append([newStart, newEnd])
                newStart, newEnd = None, None
                return res + intervals[i:]
        
        res.append([newStart, newEnd])
        
        return res