class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = set()
            col = set()
            for j in range(len(board[i])):
                if board[i][j] in row:
                    return False
                if board[j][i] in col:
                    return False
                if board[i][j] != ".":
                    row.add(board[i][j])
                if board[j][i] != ".":
                    col.add(board[j][i])
                    
        def validate3x3(rs, re, cs, ce):
            seen = set()
            for i in range(rs, re):
                for j in range(cs, ce):
                    if board[i][j] in seen:
                        return False
                    if board[i][j] != ".":
                        seen.add(board[i][j])
            return True
        
        indexes = [[0,3,0,3], [0,3,3,6], [0,3,6,9], [3,6,0,3], [3,6,3,6], [3,6,6,9], [6,9,0,3], [6,9,3,6], [6,9,6,9]]
        for rs, re, cs, ce in indexes:
            if not validate3x3(rs, re, cs, ce):
                return False
        return True