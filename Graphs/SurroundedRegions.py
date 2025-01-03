# https://neetcode.io/problems/surrounded-regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        visited = set()
        def surroundedByX(r, c) -> bool:
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return False
            if board[r][c] == 'X' or (r, c) in visited:
                return True
            visited.add((r, c))
            top = surroundedByX(r - 1, c)
            bot = surroundedByX(r + 1, c)
            left = surroundedByX(r, c - 1)
            right = surroundedByX(r, c + 1)
            print(r, c, top and bot and left and right)
            return top and bot and left and right

        def fillX(coords):
            for r, c in coords:
                board[r][c] = 'X'
    
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O' and (r, c) not in visited and surroundedByX(r, c):
                    fillX(visited)
                visited = set()