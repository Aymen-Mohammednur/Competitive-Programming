class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        1 to 0 - A
        0 to 1 = B
        """
        directions = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        def inBound(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                live = 0
                for x, y in directions:
                    if inBound(i + x, j + y):
                        if board[i + x][j + y] == 1 or board[i + x][j + y] == 'A':
                            live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 'A'
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 'B'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 0
                elif board[i][j] == 'B':
                    board[i][j] = 1
        