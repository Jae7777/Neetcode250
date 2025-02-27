# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}
        for i, c in enumerate(order):
            rank[c] = i
        for i in range(0, len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            j = 0
            n = min(len(word1), len(word2))
            while j < n:
                if rank[word1[j]] > rank[word2[j]]:
                    return False
                elif rank[word1[j]] < rank[word2[j]]:
                    break
                else:
                    j += 1
            if j == n and len(word1) > len(word2):
                return False
        return True