# https://leetcode.com/problems/meeting-rooms-iii/description/

from typing import List
import heapq
# TIME: O(n * log(n)), n is the number of meetings
# SPACE: O(n)

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n # room index, use count
        emptyRooms = [i for i in range(n)] # room index
        filledRooms = [] # end time, room index
        for start, end in meetings:
            while filledRooms and filledRooms[0][0] <= start:
                heapq.heappush(emptyRooms, heapq.heappop(filledRooms)[1])
            if not emptyRooms:
                roomEnd, roomIndex = heapq.heappop(filledRooms)
                heapq.heappush(filledRooms, (max(start, roomEnd) + (end - start), roomIndex))
            else:
                roomIndex = heapq.heappop(emptyRooms)
                heapq.heappush(filledRooms, (end, roomIndex))
            count[roomIndex] += 1
        maxUses, i = 0, 0
        for j, uses in enumerate(count):
            if uses > maxUses:
                maxUses = uses
                i = j
        return i