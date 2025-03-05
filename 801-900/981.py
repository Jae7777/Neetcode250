# https://neetcode.io/problems/time-based-key-value-store
# https://leetcode.com/problems/time-based-key-value-store/description/
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        l, r = 0, len(self.tm[key]) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            t = self.tm[key][m][1]
            if t < timestamp:
                res = self.tm[key][m][0]
                l = m + 1
            elif t > timestamp:
                r = m - 1
            else:
                return self.tm[key][m][0]
        return res
                

