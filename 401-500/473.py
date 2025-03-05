# https://leetcode.com/problems/matchsticks-to-square/
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sumLength = sum(matchsticks)
        if sumLength % 4 != 0:
            return False
        sideLength = sumLength // 4
        if max(matchsticks) > sideLength:
            return False
        sides = [0] * 4
        matchsticks.sort(reverse=True)
        def formSquare(i):
            if i == len(matchsticks):
                return True
            for j, side in enumerate(sides):
                if side + matchsticks[i] <= sideLength:
                    sides[j] += matchsticks[i]
                    if formSquare(i + 1):
                        return True
                    sides[j] = side
            return False
        return formSquare(0)
  
solution = Solution()
tests = [
  ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], True),
  ([13,11,1,8,6,7,8,8,6,7,8,9,8], True),
  ([1,1,2,2,2], True),
  ([3,3,3,3,4], False),
  ([4,13,1,1,14,15,1,3,13,1,3,5,2,8,12], True)
]
for test, expected in tests:
    assert(solution.makesquare(test) == expected)
print("tests passed")