# https://neetcode.io/problems/longest-consecutive-sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            count = 0
            l, r = n - 1, n
            while r in s:
                count += 1
                s.remove(r)
                r += 1
            while l in s:
                count += 1
                s.remove(l)
                l -= 1
            res = max(res, count)
        return res