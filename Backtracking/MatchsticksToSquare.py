# https://leetcode.com/problems/matchsticks-to-square/
from collections import defaultdict
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sumLength = sum(matchsticks)
        if sumLength % 4 != 0:
            return False
        sideLength = sumLength // 4
        if max(matchsticks) > sideLength:
            return False
        count = defaultdict(int)
        for match in sorted(matchsticks)[::-1]:
            count[match] += 1
        def formSqaure(currLength, sidesFormed):
            if sidesFormed == 4:
                return True
            if currLength == sideLength:
                return formSqaure(0, sidesFormed + 1)
            if currLength > sideLength:
                return False
            for match in count:
                if count[match] > 0:
                    count[match] -= 1
                    if formSqaure(currLength + match, sidesFormed):
                        return True
                    count[match] += 1
            return False
        return formSqaure(0, 0)
  
solution = Solution()
tests = [
  ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], True),
  ([13,11,1,8,6,7,8,8,6,7,8,9,8], True),
  ([1,1,2,2,2], True),
  ([3,3,3,3,4], False)
]
for test, expected in tests:
    assert(solution.makesquare(test) == expected)
print("tests passed")