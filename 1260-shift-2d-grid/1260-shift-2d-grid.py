class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        temp = grid[0][0]        
        for l in range(k):
            for i in range(m):
                for j in range(n):
                    grid[i][j], temp = temp, grid[i][j]
            grid[0][0] = temp
        return grid