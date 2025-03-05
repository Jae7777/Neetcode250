# https://leetcode.com/problems/ipo/
from typing import List
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_pq = []
        profit_pq = []
        for profit, capital in zip(profits, capital):
            heapq.heappush(capital_pq, (capital, profit))
        while k > 0:
            while capital_pq and w >= capital_pq[0][0]:
                _, profit = heapq.heappop(capital_pq)
                heapq.heappush(profit_pq, -profit)
            w += -heapq.heappop(profit_pq) if profit_pq else 0
            k -= 1
        return w