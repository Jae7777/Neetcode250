# https://leetcode.com/problems/dota2-senate/
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQ, dQ = deque(), deque()
        for i, sen in enumerate(senate):
            if sen == 'R':
                rQ.append(i)
            else:
                dQ.append(i)
        i = len(senate)
        while rQ and dQ:
            r = rQ.popleft()
            d = dQ.popleft()
            if r < d:
                rQ.append(i)
            else:
                dQ.append(i)
            i += 1
        return 'Radiant' if rQ else 'Dire'