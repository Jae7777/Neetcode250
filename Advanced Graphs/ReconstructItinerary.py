# https://neetcode.io/problems/reconstruct-flight-path
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in sorted(tickets)[::-1]:
            graph[u].append(v)
        res = []
        def dfs(u):
            while graph[u]:
                v = graph[u].pop()
                dfs(v)
            res.append(u)

        dfs('JFK')
        return res[::-1]