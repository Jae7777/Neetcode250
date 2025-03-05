# https://neetcode.io/problems/valid-tree
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited = set()
        def isTree(u, parent):
            if u in visited:
                return False
            visited.add(u)
            for v in adjList[u]:
                if v == parent:
                    continue
                if not isTree(v, u):
                    return False
            return True
        
        return isTree(edges[0][0] if edges else 0, -1) and len(visited) == n