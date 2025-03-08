# https://neetcode.io/problems/design-word-search-data-structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class Node:
    def __init__(self):
        self.next = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        d = self.root
        for c in word:
            if c not in d.next:
                d.next[c] = Node()
            d = d.next[c]
        d.isWord = True

    def search(self, word: str) -> bool:
        def dfs(d, i):
            if i == len(word):
                return d.isWord
            if word[i] == '.':
                for c in d.next:
                    if dfs(d.next[c], i + 1):
                        return True
            else:
                if word[i] in d.next:
                    return dfs(d.next[word[i]], i + 1)
            return False
        
        return dfs(self.root, 0)
