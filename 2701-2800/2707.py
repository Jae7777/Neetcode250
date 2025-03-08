# https://leetcode.com/problems/extra-characters-in-a-string/

from typing import List

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.next = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s):
        curr = self.root
        for c in s:
            if c not in curr.next:
                curr.next[c] = TrieNode()
            curr = curr.next[c]
        curr.isWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        memo = {len(s): 0}
        def dfs(i):
            if i in memo:
                return memo[i]
            res = 1 + dfs(i + 1)
            j = i
            curr = trie.root
            while j < len(s) and s[j] in curr.next:
                curr = curr.next[s[j]]
                j += 1
                if curr.isWord:
                    res = min(res, dfs(j))
            memo[i] = res
            return res
        return dfs(0)