# https://leetcode.com/problems/candy/

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        i, j = 0, 1
        # [1,2,3,3,4,2,6,5,4,3,5]
        # [1,2,3,1,2,1,2,1,1,1,2] # prefix
        # [1,2,3,1,2,1,4,3,2,1,2] # suffix
        while j < n:
            if ratings[j] > ratings[i]:
                candies[j] = candies[i] + 1
            i += 1
            j += 1
            
        i, j = n - 2, n - 1
        while i >= 0:
            if ratings[i] > ratings[j]:
                candies[i] = max(candies[i], candies[j] + 1)
            i -= 1
            j -= 1
        
        return sum(candies)