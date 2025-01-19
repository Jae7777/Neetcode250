# https://leetcode.com/problems/find-k-closest-elements/description/
class Solution: # sliding window
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dist = 0
        l = r = 0
        while r < k:
            dist += abs(x - arr[r])
            r += 1
        res = (l, r)
        minDist = dist
        while r < len(arr):
            dist += abs(x - arr[r])
            dist -= abs(x - arr[l])
            r += 1
            l += 1
            if dist < minDist:
                minDist = dist
                res = (l, r)
        return arr[res[0]:res[1]]

