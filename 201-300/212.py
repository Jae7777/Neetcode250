# https://neetcode.io/problems/search-for-word-ii
# https://leetcode.com/problems/word-search-ii/description/

from typing import List

class TrieNode:
    def __init__(self):
        self.next = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        d = self.root
        for c in word:
            if c not in d.next:
                d.next[c] = TrieNode()
            d = d.next[c]
        d.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        currPath = {} # ordered dict
        searched = set()
        ROW, COL = len(board), len(board[0])
        def search(d: TrieNode, r: int, c: int) -> None:
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in currPath:
                return
            letter = board[r][c]
            if letter not in d.next:
                return 
            d = d.next[letter]
            currPath[(r, c)] = None
            if d.isWord:
                word = []
                for path in currPath.keys():
                    searched.add((path[0], path[1]))
                    word.append(board[path[0]][path[1]])
                res.append("".join(word))
                d.isWord = False
            search(d, r - 1, c)
            search(d, r + 1, c)
            search(d, r, c - 1)
            search(d, r, c + 1)
            del currPath[(r, c)]

        root = trie.root
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] in root.next:
                    search(root, r, c)
        return res

        