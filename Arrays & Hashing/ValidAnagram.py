# https://neetcode.io/problems/is-anagramclass Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)