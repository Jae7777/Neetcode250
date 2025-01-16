# https://leetcode.com/problems/sort-an-array/description/
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def merge(self, nums, l, m, r):
        sortedNums = []
        i1, i2 = l, m + 1
        while i1 <= m and i2 <= r:
            if nums[i1] < nums[i2]:
                sortedNums.append(nums[i1])
                i1 += 1
            else:
                sortedNums.append(nums[i2])
                i2 += 1
        for i in range(i1, m + 1):
            sortedNums.append(nums[i])
        for i in range(i2, r + 1):
            sortedNums.append(nums[i])
        for num in sortedNums:
            nums[l] = num
            l += 1

    def mergeSort(self, nums, l, r):
        if l >= r:
            return
        m = (l + r) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m + 1, r)
        self.merge(nums, l, m, r)