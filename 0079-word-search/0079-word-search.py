class Solution:
    def __init__(self):
        self.isTrue = False
        
    def inBound(self, row, col, ROWS, COLS):
        return 0 <= row < ROWS and 0 <= col < COLS
    
    def dfs(self, board, i, j, word, visited, directions, ROWS, COLS, index):
        if index == len(word):
            self.isTrue = True
            return True
        temp = board[i][j]
        board[i][j] = '#'
        res = False
        for x, y in directions:
            nr, nc = x + i, y + j
            if self.inBound(nr, nc, ROWS, COLS) and board[nr][nc] != '#':
                if not self.isTrue and board[nr][nc] == word[index]:
                    self.dfs(board, nr, nc, word, visited, directions, ROWS, COLS, index + 1)
        board[i][j] = temp
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    self.dfs(board, i, j, word, set(), directions, ROWS, COLS, 1)
                    if self.isTrue:
                        return True
        return False