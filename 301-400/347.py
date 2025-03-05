# https://neetcode.io/problems/top-k-elements-in-list
# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        counter = Counter(nums)
        for key, val in counter.items():
            freq[val].append(key)
        res = []
        for li in freq[::-1]:
            for n in li:
                if len(res) == k: return res
                res.append(n)
        return res
