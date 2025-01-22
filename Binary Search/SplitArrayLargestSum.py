https://leetcode.com/problems/split-array-largest-sum/
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = -(sum(nums) // -k), -(max(nums) * len(nums) // -k)
        res = float('inf')
        while l <= r:
            maxSum = 0
            m = (l + r) // 2
            currSum = 0
            subarrays = 1
            for num in nums:
                if currSum + num <= m:
                    currSum += num
                else:
                    maxSum = max(maxSum, currSum)
                    currSum = num
                    subarrays += 1
            maxSum = max(maxSum, currSum)
            if subarrays > k:
                l = m + 1
            else:
                r = m - 1
                res = maxSum
        return res
