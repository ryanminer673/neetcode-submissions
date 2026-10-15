"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        starts = []
        ends = []

        for interval in intervals:
            start = interval.start
            end = interval.end
            starts.append(start)
            ends.append(end)

        starts.sort()
        ends.sort()

        s=0
        e=0
        max_rooms = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                max_rooms += 1
            else:
                e += 1
                max_rooms -= 1
            
            if max_rooms > 1:
                return False

        return True







