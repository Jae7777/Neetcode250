# https://neetcode.io/problems/car-fleet
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = sorted(zip(position, speed))
        res = 0
        limit = float('-inf')
        while stack:
            ps = stack.pop()
            time = (target - ps[0]) / ps[1]
            if time <= limit:
                continue
            limit = time
            res += 1
        return res