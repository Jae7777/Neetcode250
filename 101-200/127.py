# https://neetcode.io/problems/word-ladder
# https://leetcode.com/problems/word-ladder/description/
from typing import List
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + '*' + word[i+1:]].add(word)
        q = deque([beginWord])
        res = 0
        while q:
            newQ = deque()
            res += 1
            while q:
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    wildcard = word[:i] + '*' + word[i+1:]
                    if wildcard in graph:
                        for nextWord in graph[wildcard]:
                            newQ.append(nextWord)
                        del graph[wildcard]
            q = newQ
        return 0