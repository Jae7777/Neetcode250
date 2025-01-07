# https://neetcode.io/problems/word-break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        isWord = [False] * (len(s) + 1)
        isWord[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i - len(word) >= 0 and s[i - len(word) : i] == word:
                    isWord[i] = isWord[i - len(word)]
                if isWord[i]:
                    break
        return isWord[-1]