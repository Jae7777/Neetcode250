# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = None, 1
        for num in nums:
            if num != majority:
                count -= 1
                if count == 0:
                    majority = num
                    count = 1
            else:
                count += 1
        return majority