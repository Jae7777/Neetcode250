# https://neetcode.io/problems/subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res += [subset + [n] for subset in res]
        return res