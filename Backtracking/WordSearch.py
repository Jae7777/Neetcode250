# https://neetcode.io/problems/search-for-word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        searched = set()
        def wordSearch(br, bc, wi):
            if wi == len(word):
                return True
            if br < 0 or br >= len(board) or bc < 0 or bc >= len(board[br]):
                return False
            if (br, bc) in searched or board[br][bc] != word[wi]:
                return False
            searched.add((br, bc))
            b1 = wordSearch(br-1, bc, wi + 1)
            b2 = wordSearch(br+1, bc, wi + 1)
            b3 = wordSearch(br, bc-1, wi + 1)
            b4 = wordSearch(br, bc+1, wi + 1)
            searched.remove((br, bc))
            return b1 or b2 or b3 or b4

        for r in range(len(board)):
            for c in range(len(board[r])):
                if wordSearch(r, c, 0):
                    return True
        return False