# https://leetcode.com/problems/majority-element-ii/
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # [1,9,5,6,1,2,0,1]
        can1 = can2 = None
        cnt1 = cnt2 = 0
        for num in nums:
            if num == can1:
                cnt1 += 1
            elif num == can2:
                cnt2 += 1
            elif cnt1 == 0:
                can1 = num
                cnt1 = 1
            elif cnt2 == 0:
                can2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        res = []
        threshold = len(nums) // 3
        cnt1 = cnt2 = 0
        for num in nums:
            if num == can1:
                cnt1 += 1
            if num == can2:
                cnt2 += 1
        if cnt1 > threshold:
            res.append(can1)
        if cnt2 > threshold:
            res.append(can2)
        return res
