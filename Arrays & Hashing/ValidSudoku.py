# https://neetcode.io/problems/valid-sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        for r, li in enumerate(board):
            for c, num in enumerate(li):   
                if num == '.': continue
                if num in rows[r] or num in cols[c] or num in boxes[tuple([r // 3, c // 3])]: 
                    return False
                rows[r].add(num)
                cols[c].add(num)
                boxes[tuple([r // 3, c // 3])].add(num)
        return True
