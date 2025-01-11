# https://neetcode.io/problems/merge-intervals
class Solution: # O(nlogn) time, O(n) space
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for interval in intervals:
            # | a b |
            if res and interval[0] <= res[-1][0] and interval[1] >= res[-1][1]:
                res.pop()
                res.append(interval)

            elif not res:
                res.append(interval)
                continue
            # | | a b
            elif interval[1] < res[-1][0]:
                n = res.pop()
                res.append(interval)
                res.append(n)
            # | a | b
            elif interval[0] <= res[-1][0] and interval[1] >= res[-1][0]:
                res[-1] = [interval[0], max(interval[1], res[-1][1])]
            # a | | b
            elif interval[0] >= res[-1][0] and interval[1] <= res[-1][1]:
                continue
            # a | b |
            elif interval[0] <= res[-1][1] and interval[1] >= res[-1][1]:
                res[-1] = [min(res[-1][0], interval[0]), interval[1]]
            # a b | |
            else:
                res.append(interval)
        return res