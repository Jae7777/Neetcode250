# https://neetcode.io/problems/redundant-connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [u for u in range(len(edges) + 1)]
        ranks = [1] * (len(edges) + 1)
        def find(u):
            while parents[u] != u:
                parents[u] = parents[parents[u]]
                u = parents[u]
            return u

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            if ranks[pu] >= ranks[pv]:
                parents[pv] = parents[pu]
                ranks[pu] += ranks[pv]
            else:
                parents[pu] = parents[pv]
                ranks[pv] += ranks[pu]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]