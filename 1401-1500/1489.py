# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/
# TIME: O(E^2)
# SPACE: O(E)
class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, u):
        while u != self.par[u]:
            self.par[u] = self.par[self.par[u]]
            u = self.par[u]
        return u
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] < self.rank[pv]:
            self.par[pu] = self.par[pv]
            self.rank[pv] += self.rank[pu]
        else:
            self.par[pv] = self.par[pu]
            self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted([(edge[2], i, edge[0], edge[1]) for i, edge in enumerate(edges)])
        # [(1,0,1),(1,1,2),(2,2,3),(2,0,3),(3,0,4),(3,3,4),(6,1,4)]
        minWeight = 0
        dsu = DSU(n)
        for w, i, u, v in edges:
            if dsu.union(u, v):
                minWeight += w
        critical = []
        pseudo = []
        for w1, i1, u1, v1 in edges:
            weight = 0
            dsu = DSU(n)
            for w2, i2, u2, v2 in edges:
                if i1 != i2 and dsu.union(u2, v2):
                    weight += w2
            if weight > minWeight or max(dsu.rank) != n:
                critical.append(i1)
                continue
            
            dsu = DSU(n)
            dsu.union(u1, v1)
            weight = w1
            for w2, i2, u2, v2 in edges:
                if dsu.union(u2, v2):
                    weight += w2
            if weight == minWeight:
                pseudo.append(i1)
        return [critical, pseudo]