# https://leetcode.com/problems/subarray-sum-equals-k
from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int)
        prefixes[0] = 1
        currSum = 0
        res = 0
        for num in nums:
            currSum += num
            if currSum - k in prefixes:
                res += prefixes[currSum - k]
            prefixes[currSum] += 1
        return res