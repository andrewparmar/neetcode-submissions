"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])

        s, e = 0, 0

        count = 0
        max_count = 0

        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            elif starts[s] >= ends[e]:
                count -= 1
                e += 1
            # elif starts[s] == ends[e]:
            #     count -= 1
            #     e += 1
            max_count = max(max_count, count)

        return max_count
