# https://leetcode.com/problems/longest-happy-string/
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(pq)
        res = []
        while pq:
            cnt, c = heapq.heappop(pq)
            if not res or res[-1] != c:
                i = max(cnt, -2)
                while i < 0:
                    res.append(c)
                    i += 1
                if cnt + 2 < 0:
                    heapq.heappush(pq, (cnt + 2, c))
            elif pq:
                cnt2, c2 = heapq.heappop(pq)
                i = max(cnt2, -1)
                while i < 0:
                    res.append(c2)
                    i += 1
                if cnt2 + 1 < 0:
                    heapq.heappush(pq, (cnt2 + 1, c2))
                heapq.heappush(pq, (cnt, c))
            else:
                break
        return ''.join(res)