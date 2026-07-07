from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       rows = defaultdict(set)
       columns = defaultdict(set)
       squares = defaultdict(set)

       for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue

            if (board[r][c] == rows[r] | board[r][c] == columns[c] | board[r][c] == squares[(r // 3, c // 3)]):
                return False
            
            columns[c].add(board[r][c])
            rows[r].add(board[r][c])
            sqaures[(r//3, c//3)].add(board[r][c])

        return True
