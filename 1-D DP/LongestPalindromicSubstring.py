# https://neetcode.io/problems/longest-palindromic-substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = set()
        longest = (0, 0)
        def findPalindromes(l, r):
            nonlocal longest
            if l < 0 or r >= len(s):
                return
            if l == r or (s[l] == s[r] and (l == r - 1 or (l + 1, r - 1) in palindromes)):
                palindromes.add((l, r))
                if r - l > longest[1] - longest[0]:
                    longest = (l, r)
                findPalindromes(l - 1, r + 1)
            return
        
        for i in range(len(s) - 1):
            findPalindromes(i, i)
            findPalindromes(i, i + 1)
        return s[longest[0]:longest[1]+1]