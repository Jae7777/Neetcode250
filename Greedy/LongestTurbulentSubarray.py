# https://leetcode.com/problems/longest-turbulent-subarray/
# Runtime: beats 27.54%
# Memory: beats 30.11%
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        inc, dec = 1, 1
        res = 1
        for i in range(1, len(arr)):
            if arr[i - 1] == arr[i]:
                inc, dec = 1, 1
            elif arr[i - 1] < arr[i]:
                inc = dec + 1
                dec = 1
            else:
                dec = inc + 1
                inc = 1
            res = max(res, max(inc, dec))
        return res
    
# Runtime: beats 95.55%
# Memory: beats 48.96%
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