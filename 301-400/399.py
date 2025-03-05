# https://leetcode.com/problems/evaluate-division/
from collections import defaultdict
from typing import List

# compute path on the fly
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i, edge in enumerate(equations):
            u, v = edge
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]
        visited = set()
        def dfs(u, target, val):
            if u in visited:
                return -1.0
            if target in graph[u]:
                return val * graph[u][target]
            visited.add(u)
            for v in graph[u]:
                res = dfs(v, target, val * graph[u][v])
                if res != -1.0:
                    return res
            return -1.0
        res = []
        for u, v in queries:
            res.append(dfs(u, v, 1.0))
            visited = set()
        return res
    
# pre compute all paths for efficient queries, exceeds LC memory constraint
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i, edge in enumerate(equations):
            u, v = edge
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]
        for u in list(graph.keys()):
            visited = set()
            q = [(u, 1.0)]
            while q:
                u1, val1 = q.pop()
                if (u1, val1) in visited:
                    continue
                visited.add((u1, val1))
                for u2 in graph[u1]:
                    val2 = graph[u1][u2]
                    q.append((u2, val2 * val1))
            for v, val in visited:
                graph[u][v] = val
        res = []
        for u, v in queries:
            if u not in graph or v not in graph[u]:
                res.append(-1.0)
            else:
                res.append(graph[u][v])
        return res