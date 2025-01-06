# https://neetcode.io/problems/maximum-product-subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane's algo
        res = currMin = currMax = nums[0]
        for num in nums[1:]:
            tmp = currMax
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(tmp * num, currMin * num, num)
            res = max(res, currMax)
        return res