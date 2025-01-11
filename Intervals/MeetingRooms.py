# https://neetcode.io/problems/meeting-schedule
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda interval: interval.start)
        last = intervals[0]
        for interval in intervals[1:]:
            if interval.start < last.end:
                return False
            last = interval
        return True