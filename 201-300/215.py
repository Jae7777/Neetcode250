# https://neetcode.io/problems/kth-largest-element-in-an-array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, n)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]