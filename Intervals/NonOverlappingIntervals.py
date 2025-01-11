# https://neetcode.io/problems/non-overlapping-intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] < prev[1]: 
                res += 1
                if interval[1] >= prev[1]:
                    continue
            prev = interval
        return res