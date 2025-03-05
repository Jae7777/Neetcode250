# https://leetcode.com/problems/word-break-ii/
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        currSentence = []
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(currSentence))
                return
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in wordDict:
                    currSentence.append(word)
                    backtrack(j)
                    currSentence.pop()
        backtrack(0)
        return res