# https://neetcode.io/problems/products-of-array-discluding-self
# https://leetcode.com/problems/product-of-array-except-self/description/
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res, prefix, suffix = [0] * N, [1] * N, [1] * N
        for i in range(N - 1):
            prefix[i+1] *= prefix[i] * nums[i]
        for i in range(N - 1, 0, -1):
            suffix[i-1] *= suffix[i] * nums[i]
        for i in range(N):
            res[i] = prefix[i] * suffix[i]
        return res