class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range (9):
            current_row = rows[r]
            
            for c in range (9):
                current_col = cols[c]
                current_sq = squares[(r // 3, c // 3)]
                current_val = board[r][c]

                if current_val == ".":
                    continue
                    
                if ( current_val in current_row or
                     current_val in current_col or
                     current_val in current_sq ):
                     return False

                current_row.add(current_val)
                current_col.add(current_val)
                current_sq.add(current_val)
        
        return True
        