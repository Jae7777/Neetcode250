# https://neetcode.io/problems/non-cyclical-number
# O(logn) time, O(logn) space
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            currSum = 0
            for c in str(n):
                currSum += int(c) ** 2
            if currSum == 1:
                return True
            if currSum in visited:
                return False
            visited.add(currSum)
            n = currSum

# O(logn) time, O(1) space
class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquares(num):
            currSum = 0
            for c in str(num):
                currSum += int(c) ** 2
            return currSum
        
        slow, fast = n, sumSquares(n)
        while slow != fast:
            fast = sumSquares(sumSquares(fast))
            slow = sumSquares(slow)
        return fast == 1