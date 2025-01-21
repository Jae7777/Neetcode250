# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight = max(weights)
        l, r = maxWeight, len(weights) * maxWeight
        minCap = float('inf')
        while l <= r:
            cap = (l + r) // 2
            cycles = 0
            currCap = 0
            for w in weights:
                currCap += w
                if currCap > cap:
                    cycles += 1
                    currCap = w
                elif currCap == cap:
                    cycles += 1
                    currCap = 0
            cycles += 1 if currCap else 0
            if cycles <= days:
                minCap = cap
                r = cap - 1
            else:
                l = cap + 1
        return minCap
            