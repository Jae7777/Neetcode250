# https://leetcode.com/problems/interleaving-string/submissions/1562157851/
# 2-D DP
# TIME: O(N*M)
# SPACE: O(N*M)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        memo = set()
        def dfs(i, j, k):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in memo:
                return False
            memo.add((i, j))
            a = b = False
            if i < len(s1) and s1[i] == s3[k]:
                a = dfs(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                b = dfs(i, j + 1, k + 1)
            return a or b
            
        return dfs(0, 0, 0)