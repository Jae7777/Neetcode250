# https://neetcode.io/problems/palindromic-substrings
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