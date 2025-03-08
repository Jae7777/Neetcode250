# https://leetcode.com/problems/closest-prime-numbers-in-range/description/

# INITIAL SOLUTION, SPACE OPTIMIZED
# TIME: O(n * sqrt(n)) where n is the range of numbers
# SPACE: O(1)
from typing import List
from collections import deque
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        q = deque()
        shortest = float('inf')
        res = [-1, -1]
        limit = right + 1
        for i in range(max(2, left), right + 1):
            if i == limit:
                break
            j = 2
            stop = int(i ** 0.5) + 1
            while j < stop:
                if i % j == 0:
                    break
                j += 2 if j != 2 else 1
            if j >= stop:
                q.append(i)
            if len(q) > 2:
                q.popleft()
                if q[1] - q[0] < shortest:
                    res[0], res[1] = q[0], q[1]
                    shortest = q[1] - q[0]
            elif len(q) == 2 and res == [-1, -1]:
                shortest = q[1] - q[0]
                res[0], res[1] = q[0], q[1]
                limit = q[0] * q[1]
        return res