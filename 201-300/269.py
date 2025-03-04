# https://neetcode.io/problems/foreign-dictionary
# graph
# TIME: O(n * m), n = len(words), m = max(len(word))
# SPACE: O(n * m)
from typing import List
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for c1, c2 in zip(word1, word2):
                if c1 == c2 and len(word1) > len(word2):
                    return ""
                if c1 != c2:
                    graph[c1].add(c2)
                    break
        
        res = []
        visited = {}
        def endTraverse(u):
            if u in visited:
                return visited[u]
            visited[u] = True
            if u in graph:
                for v in graph[u]:
                    if endTraverse(v):
                        return True
            visited[u] = False
            res.append(u)
            return False
        
        for u in graph:
            print(u)
            if endTraverse(u):
                return ""

        return "".join(res[::-1])