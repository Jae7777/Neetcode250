# https://leetcode.com/problems/edit-distance/submissions/1562121443/
# 2-D DP
# TIME: O(N*M)
# SPACE: O(N*M)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        edits = [[0] * (M + 1) for _ in range(N + 1)]
        edits[N][M] = 0
        for i in range(N - 1, -1, -1):
            edits[i][M] = N - i
        for j in range(M - 1, -1, -1):
            edits[N][j] = M - j
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if word1[i] != word2[j]:
                    edits[i][j] = 1 + min(edits[i + 1][j], edits[i][j + 1], edits[i + 1][j + 1])
                else:
                    edits[i][j] = edits[i + 1][j + 1]
                    
        return edits[0][0]