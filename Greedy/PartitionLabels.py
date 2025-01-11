# https://neetcode.io/problems/partition-labels
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        q = set([s[0]])
        res = [0]
        last = -1
        for i, c in enumerate(s):
            count[c] -= 1
            if count[c] == 0:
                if c in q:
                    q.remove(c)
            else:
                q.add(c)
            if not q:
                res.append(i - last)
                last = i
        
        return res[1:]