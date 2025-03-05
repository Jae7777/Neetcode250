# https://neetcode.io/problems/count-connected-components
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {u: [] for u in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        def visitCC(u):
            visited.add(u)
            for v in adjList[u]:
                if v not in visited:
                    visitCC(v)
        nCC = 0
        for u in range(n):
            if u not in visited:
                visitCC(u)
                nCC += 1
        return nCC