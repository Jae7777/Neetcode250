# https://neetcode.io/problems/minimum-interval-including-query
# https://leetcode.com/problems/minimum-interval-to-include-each-query/

from typing import List
import heapq
class Solution: 
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}
        i = 0
        pq = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            res[q] = pq[0][0] if pq else -1
        return [res[q] for q in queries]