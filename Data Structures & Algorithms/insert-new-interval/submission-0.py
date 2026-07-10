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
            print("****")
            print(currStart, currEnd)
            print(newStart, newEnd)
            if newStart <= currStart <= newEnd or currStart <= newStart <= currEnd:
                print("merging")
                newStart, newEnd = min(currStart, newStart), max(currEnd, newEnd)
                print(newStart, newEnd)
                continue
            if currEnd < newStart:
                res.append(intervals[i])
            if newEnd < currStart:
                res.append([newStart, newEnd])
                newStart, newEnd = None, None
                res = res + intervals[i:]
                return res
        
        res.append([newStart, newEnd])
        
        return res