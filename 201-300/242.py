# https://neetcode.io/problems/is-anagram
# https://leetcode.com/problems/valid-anagram/
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)