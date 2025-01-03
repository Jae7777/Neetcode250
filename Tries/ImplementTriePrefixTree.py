# https://neetcode.io/problems/implement-prefix-tree
class Node:
    def __init__(self):
        self.next = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        d = self.root
        for c in word:
            if c not in d.next:
                d.next[c] = Node()
            d = d.next[c]
        d.isWord = True

    def search(self, word: str) -> bool:
        d = self.root
        for c in word:
            if c not in d.next:
                return False
            d = d.next[c]
        return d.isWord

    def startsWith(self, prefix: str) -> bool:
        d = self.root
        for c in prefix:
            if c not in d.next:
                return False
            d = d.next[c]
        return True
        
        