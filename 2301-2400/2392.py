# https://leetcode.com/problems/build-a-matrix-with-conditions/

from typing import List

class Solution:
    def topologicalOrder(self, k, edges: List[List[int]]) -> List[int]:
        rGraph = { i: set() for i in range(1, k + 1) }
        for u, v in edges:
            rGraph[v].add(u)
        res = []
        visited = set()
        recStack = set()
        def dfs(u):
            if u in recStack:
                return False
            if u in visited:
                return True
            visited.add(u)
            recStack.add(u)
            for v in rGraph[u]:
                if not dfs(v):
                    return False
            recStack.remove(u)
            res.append(u)
            return True
            
        for u in rGraph:
            if u not in visited:
                if not dfs(u):
                    return [-1]  # Cycle detected
        return res

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowOrder = self.topologicalOrder(k, rowConditions)
        colOrder = self.topologicalOrder(k, colConditions)
        if rowOrder == [-1] or colOrder == [-1]:
            return []
        matrix = [[0 for _ in range(k)] for _ in range(k)]
        vertices = { i: [-1, -1] for i in range(1, k + 1) }
        for i, u in enumerate(rowOrder):
            vertices[u][0] = i
        for i, u in enumerate(colOrder):
            vertices[u][1] = i
        for u in vertices:
            r, c = vertices[u][0], vertices[u][1]
            if r != -1 and c != -1:
                matrix[r][c] = u
        return matrix