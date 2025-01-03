# https://neetcode.io/problems/is-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.compile('[\W_]+').sub('', s).lower()
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True