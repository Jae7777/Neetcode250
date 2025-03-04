# https://leetcode.com/problems/palindromic-substrings/
# 1-D DP
# Time: O(N^2)
# Space: O(N)
class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = set()
        def addPalindromes(l, r):
            if l < 0 or r >= len(s):
                return
            if l == r or (s[l] == s[r] and (l + 1 == r or (l + 1, r - 1) in palindromes)):
                palindromes.add((l, r))
                addPalindromes(l - 1, r + 1)
        for i in range(len(s) - 1):
            addPalindromes(i, i)
            addPalindromes(i, i + 1)
        addPalindromes(len(s) - 1, len(s) - 1)

        return len(palindromes)
  
# two pointer
# Time: O(N^2)
# Space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        def extend(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            extend(i, i)
            extend(i, i + 1)

        return palindromes