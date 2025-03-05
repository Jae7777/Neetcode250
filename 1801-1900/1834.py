# https://leetcode.com/problems/single-threaded-cpu/
from typing import List
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enqueue = []
        process = []
        res = []
        for i, task in enumerate(tasks):
            heapq.heappush(enqueue, (task[0], task[1], i))
        time = enqueue[0][0]
        while enqueue:
            while enqueue and time >= enqueue[0][0]:
                task = heapq.heappop(enqueue)
                heapq.heappush(process, (task[1], task[2]))
            if process:
                task = heapq.heappop(process)
                time += task[0]
                res.append(task[1])
            else:
                time = enqueue[0][0]
        while process:
            res.append(heapq.heappop(process)[1])
        return res