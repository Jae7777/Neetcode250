# https://neetcode.io/problems/subsets-ii
# https://leetcode.com/problems/subsets-ii/description/
from typing import List
from collections import defaultdict
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        nums = list(count.keys())
        def createSubset(used, start, currSubset):
            if len(used) == len(count):
                return
            for i, n in enumerate(nums[start:]):
                if n not in used:
                    for freq in range(count[n]):
                        res.append(currSubset + [n] * (freq + 1))
                        createSubset(used | set([n]), start + i, currSubset + [n] * (freq + 1))
        createSubset(set(), 0, [])
        return res