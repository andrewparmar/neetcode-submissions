"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        prev = Interval(-1, -1)
        
        for curr in intervals:
            if curr.start < prev.end:
                return False
            prev = curr

        return True