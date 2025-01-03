# https://neetcode.io/problems/min-cost-to-connect-points
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points[i + 1:]):
                manhattan = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                edges.append((manhattan, tuple(point1), tuple(point2)))
        parents = {tuple(point): tuple(point) for point in points}
        ranks = {tuple(point): 1 for point in points}
        def find(u):
            while u != parents[u]:
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
            
        res = 0
        for manhattan, point1, point2 in sorted(edges):
            if union(point1, point2):
                res += manhattan
        return res