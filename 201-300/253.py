# https://neetcode.io/problems/meeting-schedule-ii
"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List
import heapq

class Solution: # O(n^2) time, O(n) space
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        days = [intervals[0]]
        for interval in intervals[1:]:
            fitted = False
            for i, day in enumerate(days):
                if interval.start >= day.end:
                    days[i] = Interval(day.start, interval.end)
                    fitted = True
                    break
            if not fitted:
                days.append(interval)
        return len(days)

class Solution: # O(nlogn) time, O(n) space
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        days = []
        for interval in intervals:
            if days and days[0] <= interval.start:
                heapq.heappop(days)
            heapq.heappush(days, interval.end)
        return len(days)