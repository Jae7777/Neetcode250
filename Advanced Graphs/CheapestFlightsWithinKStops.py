# https://neetcode.io/problems/cheapest-flight-path
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(set)
        for u, v, price in flights:
            adjList[u].add((price, v))
        prices = [float('inf') for _ in range(n)]
        prices[src] = 0
        q = deque([(0, 0, src)]) # price, stop#, airport
        while q:
            uPrice, stop, u = q.popleft()
            if stop >= k + 1:
                continue
            for vPrice, v in adjList[u]:
                if uPrice + vPrice < prices[v]:
                    q.append((uPrice + vPrice, stop + 1, v))
                    prices[v] = uPrice + vPrice
                    
        return prices[dst] if prices[dst] != float('inf') else -1