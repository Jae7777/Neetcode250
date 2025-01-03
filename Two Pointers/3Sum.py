# https://neetcode.io/problems/three-integer-sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n > 0: break
            if i > 0 and n == nums[i - 1]: continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                ln, rn = nums[l], nums[r]
                threesum = ln + rn + n
                if threesum == 0:
                    res.append([ln, rn, n])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    l += 1
        return res