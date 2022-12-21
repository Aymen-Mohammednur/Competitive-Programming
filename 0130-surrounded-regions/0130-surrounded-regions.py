class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def inBound(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        def dfs(r, c):
            visited.add((r, c))
            for x, y in directions:
                nr, nc = r+x, c+y
                if inBound(nr,nc) and (nr,nc) not in visited and board[nr][nc] == 'O':
                    dfs(nr, nc)
            
        for j in range(cols):
            if board[0][j] == 'O': dfs(0, j)
            if board[rows-1][j] == 'O': dfs(rows - 1, j)

        for i in range(1, rows - 1):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][cols-1] == 'O': dfs(i, cols - 1)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'