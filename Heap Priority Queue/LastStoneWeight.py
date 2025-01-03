# https://neetcode.io/problems/last-stone-weight
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)
        while len(pq) > 1:
            x, y = heapq.heappop(pq), heapq.heappop(pq)
            weight = abs(x - y)
            heapq.heappush(pq, -weight)
        return -pq[0]