# https://neetcode.io/problems/minimum-interval-including-query
# O(n * m + k) time, O(n) space
# where n is the difference of the max interval end and min interval start,
# m is the number of intervals,
# and k is the number of queries
class Solution: 
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        numLine = [float('inf')] * (max([interval[1] for interval in intervals]) + 1)
        for interval in intervals:
            for i in range(interval[0], interval[1] + 1):
                numLine[i] = min(numLine[i], interval[1] - interval[0] + 1)
        res = []
        for query in queries:
            if query >= len(numLine) or numLine[query] == float('inf'):
                res.append(-1)
            else:
                res.append(numLine[query])
        return res