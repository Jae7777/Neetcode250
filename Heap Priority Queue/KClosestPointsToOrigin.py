# https://neetcode.io/problems/k-closest-points-to-origin
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            dist = (point[0]**2 + point[1]**2) ** 0.5
            heapq.heappush(pq, (-dist, point))
            if len(pq) > k:
                heapq.heappop(pq)
        return [item[1] for item in pq]