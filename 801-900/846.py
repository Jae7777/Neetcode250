# https://neetcode.io/problems/hand-of-straights
# https://leetcode.com/problems/hand-of-straights/description/
from typing import List
from collections import defaultdict
class Solution: # O(nlogn) time, O(n) space
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = defaultdict(int)
        for num in hand:
            count[num] += 1
        # [1: 1:, 2: 2, 3: 2, 4: 2, 5: 1]
        for num in count:
            if count[num] > 0:
                for i in range(groupSize - 1, -1, -1):
                    if count[num + i] < count[num]:
                        return False
                    count[num + i] -= count[num]
        for num in count:
            if count[num] > 0:
                return False
        return True