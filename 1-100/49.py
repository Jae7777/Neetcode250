# https://neetcode.io/problems/anagram-groups
# https://leetcode.com/problems/group-anagrams/description/
# TIME: O(N * M), N is the length of strs, M is the average length of each string
# SPACE: O(N * M)
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            d[tuple(count)].append(s)
        return [anagram for anagram in d.values()]
        