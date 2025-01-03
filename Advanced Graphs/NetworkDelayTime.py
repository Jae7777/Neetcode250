# https://neetcode.io/problems/network-delay-time
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(set)
        for u, v, t in times:
            graph[u].add((t, v))
        pq = []
        for t, v in graph[k]:
            heapq.heappush(pq, (t, v))
        visited = set([k])
        res = 0
        while pq:
            if len(visited) == n:
                break
            tu, u = heapq.heappop(pq)
            if u not in visited:
                for tv, v in graph[u]:
                    pq.append((tv + tu, v))
                visited.add(u)
            heapq.heapify(pq)
            res = tu
        return res if len(visited) == n else -1
