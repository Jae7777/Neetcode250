# https://neetcode.io/problems/insert-new-interval
# https://leetcode.com/problems/insert-interval/description/
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [newInterval]
        for interval in intervals:
            if interval[1] < res[-1][0]: # | | a b
                n = res.pop()
                res.append(interval)
                res.append(n)
            elif interval[0] <= res[-1][0] and interval[1] >= res[-1][0]: # | a | b
                res[-1] = [interval[0], max(res[-1][1], interval[1])]
            elif res[-1][0] <= interval[0] and interval[1] <= res[-1][1]: # a | | b
                continue
            elif interval[0] <= res[-1][1] and interval[1] >= res[-1][1]: # a | b |
                res[-1] = [min(res[-1][0], interval[0]), interval[1]]
            else: # a b | |
                res.append(interval)
        return res