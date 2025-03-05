# https://neetcode.io/problems/clone-graph
# https://leetcode.com/problems/clone-graph/description/
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned = {}
        q = deque([node])
        while q:
            n = q.popleft()
            if n not in cloned:
                cloned[n] = Node(n.val)
                for neighbor in n.neighbors:
                    q.append(neighbor)
        for n in cloned:
            cloned[n].neighbors = []
            for neighbor in n.neighbors:
                cloned[n].neighbors.append(cloned[neighbor])

        return cloned[node]