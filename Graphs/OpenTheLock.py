# https://leetcode.com/problems/open-the-lock/
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        visited = set()
        q = deque([('0000', 0)])
        while q:
            combo, turns = q.popleft()
            if combo in visited:
                continue
            visited.add(combo)
            if combo == target:
                return turns
            for i in range(4):
                for delta in [-1, 1]:
                    next = combo[:i] + str((int(combo[i]) + delta) % 10) + combo[i+1:]
                    if next not in deadends:
                        q.append((next, turns + 1))
        return -1
