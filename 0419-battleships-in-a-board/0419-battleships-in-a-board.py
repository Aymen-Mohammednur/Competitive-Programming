class Solution:
    def traverseVertical(self, row, col, visited, ROWS, COLS, grid):
        visited.add((row, col))
        
        if row > 0 and grid[row-1][col] == 'X':
            if (row-1, col) not in visited:
                self.traverseVertical(row-1, col, visited, ROWS, COLS, grid)
            
        if row < ROWS-1 and grid[row+1][col] == 'X':
            if (row+1, col) not in visited:
                self.traverseVertical(row+1, col, visited, ROWS, COLS, grid)
            
            
    def traverseHorizontal(self, row, col, visited, ROWS, COLS, grid):
        visited.add((row, col))
        
        if col > 0 and grid[row][col-1] == 'X':
            if (row, col-1) not in visited:
                self.traverseHorizontal(row, col-1, visited, ROWS, COLS, grid)
            
        if col < COLS-1 and grid[row][col+1] == 'X':
            if (row, col+1) not in visited:
                self.traverseHorizontal(row, col+1, visited, ROWS, COLS, grid)
            
    def countBattleships(self, grid: List[List[str]]) -> int:
        battleships = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '.' or (row, col) in visited:
                    continue
                    
                if row > 0 and grid[row-1][col] == 'x' or row < ROWS-1 and grid[row+1][col] == 'X':
                    self.traverseVertical(row, col, visited, ROWS, COLS, grid)
                    
                if col > 0 and grid[row][col-1] == 'x' or col < COLS-1 and grid[row][col+1] == 'X':
                    self.traverseHorizontal(row, col, visited, ROWS, COLS, grid)
                                
                battleships += 1
                
        return battleships