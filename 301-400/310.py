# https://leetcode.com/problems/minimum-height-trees/
# graph
# TIME: O(n + m), m is the number of edges
# SPACE: O(n + m)
from collections import defaultdict, deque
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        q = deque()
        edgCount = {}
        for u in graph:
            if len(graph[u]) == 1:
                q.append(u)
            edgCount[u] = len(graph[u])
        visited = set(q)
        while q:
            if n <= 2:
                break
            newQ = deque()
            while q:
                u = q.popleft()
                n -= 1
                for v in graph[u]:
                    edgCount[v] -= 1
                    if edgCount[v] == 1:
                        newQ.append(v)
            q = newQ
        return list(q)