# https://leetcode.com/problems/car-pooling/
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        startOrder = []
        for trip in trips:
            startOrder.append((trip[1], trip[2], trip[0]))
        startOrder.sort()
        pq = []
        currCap = 0
        for trip in startOrder:
            from_, to_, numPass = trip
            heapq.heappush(pq, (to_, numPass))
            currCap += numPass
            while pq and from_ >= pq[0][0]:
                currCap -= pq[0][1]
                heapq.heappop(pq)
            if currCap > capacity:
                return False
        return True