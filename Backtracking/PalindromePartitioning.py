# https://neetcode.io/problems/palindrome-partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
            
        res, partition = [], []
        def createPartition(l):
            if l >= len(s):
                res.append(partition.copy())
                return
            for r in range(l, len(s)):
                if isPalindrome(l, r):
                    partition.append(s[l:r+1])
                    createPartition(r + 1)
                    partition.pop()

        createPartition(0)
        return res