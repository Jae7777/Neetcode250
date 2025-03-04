# https://leetcode.com/problems/longest-common-subsequence/description/
# dp - bottom up
# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        sequences = [0] * (len(text1) + 1)
        for i in range(len(sequences)):
            sequences[i] = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, - 1, -1):
                if text1[i] == text2[j]:
                    sequences[i][j] = 1 + sequences[i + 1][j + 1]
                else:
                    sequences[i][j] = max(sequences[i + 1][j], sequences[i][j + 1])

        return sequences[0][0]
# dp - top down
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROW, COL = len(text1), len(text2)
        subsequences = {}
        
        def dfs(r, c):
            if r >= ROW or c >= COL:
                return 0
            if (r, c) in subsequences:
                return subsequences[(r, c)]
            if text1[r] == text2[c]:
                subsequences[(r, c)] = 1 + dfs(r + 1, c + 1)
            else:
                subsequences[(r, c)] = max(dfs(r + 1, c), dfs(r, c + 1))
            return subsequences[(r, c)]
                
        return dfs(0, 0)