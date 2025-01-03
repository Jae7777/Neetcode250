# https://neetcode.io/problems/rotting-fruit
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        unrotted = set()
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    unrotted.add((r, c))
                if grid[r][c] == 2:
                    q.append((r, c))
        if not unrotted:
            return 0
        def spreadRot(q, r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == 0 or grid[r][c] == 2:
                return
            grid[r][c] = 2
            q.append((r, c))
            unrotted.remove((r, c))
        
        minutes = -1
        while q:
            newQ = deque()
            while q:
                r, c = q.popleft()
                spreadRot(newQ, r - 1, c)
                spreadRot(newQ, r + 1, c)
                spreadRot(newQ, r, c - 1)
                spreadRot(newQ, r, c + 1)
            q = newQ
            minutes += 1
        return -1 if unrotted else minutes