# https://leetcode.com/problems/reorganize-string/
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        pq = []
        for c in count:
            pq.append((-count[c], c))
        heapq.heapify(pq)
        res = []
        while pq:
            cnt1, c1 = heapq.heappop(pq)
            cnt2, c2 = None, None
            if pq:
                cnt2, c2 = heapq.heappop(pq)
            if res and res[-1] == c1 and c2 == None:
                return ''
            if res and res[-1] == c1:
                heapq.heappush(pq, (cnt1, c1))
                if cnt2 < -1:
                    heapq.heappush(pq, (cnt2 + 1, c2))
                res.append(c2)
            else:
                if cnt2:
                    heapq.heappush(pq, (cnt2, c2))
                if cnt1 < -1:
                    heapq.heappush(pq, (cnt1 + 1, c1))
                res.append(c1)
        return ''.join(res)