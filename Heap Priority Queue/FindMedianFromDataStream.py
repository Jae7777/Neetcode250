# https://neetcode.io/problems/find-median-in-a-data-stream
class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # first half [1.0]
        self.minHeap = [] # last half [] 0.5

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) <= len(self.minHeap):
            if self.minHeap and self.minHeap[0] < num:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)
        else:
            if -self.maxHeap[0] > num:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        