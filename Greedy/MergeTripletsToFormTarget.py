# https://neetcode.io/problems/merge-triplets-to-form-target
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [float('-inf')] * 3
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                curr = [max(a, curr[0]), max(b, curr[1]), max(c, curr[2])]
        return curr == target