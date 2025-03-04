# https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        sign = 0
        res = 1
        prev = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if sign == 0:
                if prev == arr[i]:
                    continue
                sign = -1 if prev < arr[i] else 1
                count += 1
            elif sign == -1:
                if prev == arr[i]:
                    sign = 0
                    count = 1
                    continue
                elif prev < arr[i]:
                    sign = -1
                    count = 2
                else:
                    count += 1
                    sign = 1
            elif sign == 1:
                if prev == arr[i]:
                    sign = 0
                    count = 1
                    continue
                elif prev > arr[i]:
                    sign = 1
                    count = 2
                else:
                    count += 1
                    sign = -1
            prev = arr[i]
            res = max(res, count)
        return res