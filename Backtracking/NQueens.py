# https://neetcode.io/problems/n-queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, occupancy, currBoard = [], defaultdict(int), []
        for i in range(n):
            currBoard.append([])
            for j in range(n):
                currBoard[i].append('.')

        def solve(currQueens, rstart, cstart):
            # print(currBoard)
            if currQueens == n:
                res.append(["".join(row) for row in currBoard])
                return
            for r in range(rstart, n):
                for c in range(cstart, n):
                    if occupancy[(r, c)] == 0:
                        self.placeQueen(occupancy, currBoard, n, r, c)
                        solve(currQueens + 1, r + 1, cstart)
                        self.removeQueen(occupancy, currBoard, n, r, c)
            
        solve(0, 0, 0)
        return res
    
    def placeQueen(self, occupancy, currBoard, n, r, c):
        currBoard[r][c] = 'Q'
        occupancy[(r, c)] += 1
        self.fillTopLeft(occupancy, n, r - 1, c - 1)
        self.fillTop(occupancy, n, r - 1, c)
        self.fillTopRight(occupancy, n, r - 1, c + 1)
        self.fillRight(occupancy, n, r, c + 1)
        self.fillBotRight(occupancy, n, r + 1, c + 1)
        self.fillBot(occupancy, n, r + 1, c)
        self.fillBotLeft(occupancy, n, r + 1, c - 1)
        self.fillLeft(occupancy, n, r, c - 1)
    
    def removeQueen(self, occupancy, currBoard, n, r, c):
        currBoard[r][c] = '.'
        occupancy[(r, c)] -= 1
        self.removeTopLeft(occupancy, n, r - 1, c - 1)
        self.removeTop(occupancy, n, r - 1, c)
        self.removeTopRight(occupancy, n, r - 1, c + 1)
        self.removeRight(occupancy, n, r, c + 1)
        self.removeBotRight(occupancy, n, r + 1, c + 1)
        self.removeBot(occupancy, n, r + 1, c)
        self.removeBotLeft(occupancy, n, r + 1, c - 1)
        self.removeLeft(occupancy, n, r, c - 1)

    def fillTopLeft(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] += 1
        self.fillTopLeft(occupancy, n, r - 1, c - 1)
    
    def removeTopLeft(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] -= 1
        self.removeTopLeft(occupancy, n, r - 1, c - 1)
    
    def fillTop(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] += 1
        self.fillTop(occupancy, n, r - 1, c)
    
    def removeTop(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] -= 1
        self.removeTop(occupancy, n, r - 1, c)
    
    def fillTopRight(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] += 1
        self.fillTopRight(occupancy, n, r - 1, c + 1)

    def removeTopRight(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] -= 1
        self.removeTopRight(occupancy, n, r - 1, c + 1)
    
    def fillRight(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] += 1
        self.fillRight(occupancy, n, r, c + 1)
    
    def removeRight(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] -= 1
        self.removeRight(occupancy, n, r, c + 1)
    
    def fillBotRight(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] += 1
        self.fillBotRight(occupancy, n, r + 1, c + 1)
    
    def removeBotRight(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] -= 1
        self.removeBotRight(occupancy, n, r + 1, c + 1)
    
    def fillBot(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] += 1
        self.fillBot(occupancy, n, r + 1, c)
    
    def removeBot(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] -= 1
        self.removeBot(occupancy, n, r + 1, c)
    
    def fillBotLeft(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] += 1
        self.fillBotLeft(occupancy, n, r + 1, c - 1)
    
    def removeBotLeft(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] -= 1
        self.removeBotLeft(occupancy, n, r + 1, c - 1)
    
    def fillLeft(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] += 1
        self.fillLeft(occupancy, n, r, c - 1)
    
    def removeLeft(self, occupancy, n, r, c):
        if min(r, c) < 0 or max(r, c) >= n:
            return
        occupancy[(r, c)] -= 1
        self.removeLeft(occupancy, n, r, c - 1)