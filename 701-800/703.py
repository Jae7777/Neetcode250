# https://neetcode.io/problems/kth-largest-integer-in-a-stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]
