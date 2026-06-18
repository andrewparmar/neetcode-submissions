"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        days = [[intervals[0]]]

        for intrvl in intervals[1:]:
            flag = True
            for day in days:
                if day[-1].end <= intrvl.start:
                    day.append(intrvl)
                    flag = False
                    break
            if flag:
                days.append([intrvl])
        
        return len(days)

