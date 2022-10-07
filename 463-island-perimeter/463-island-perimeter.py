class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        n, m = len(grid), len(grid[0])
        def inBound(r, c):
            return 0 <= r < n and 0 <= c < m
        visited = set()
        perimeter = 0
        def dfs(r, c):
            nonlocal perimeter
            visited.add((r,c))
            for x, y in directions:
                if not inBound(x+r, y+c) or grid[x+r][y+c] == 0:
                    perimeter += 1
                elif inBound(x+r, y+c) and grid[x+r][y+c] == 1 and (x+r,y+c) not in visited:
                    dfs(x + r, y + c)
            return perimeter
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i,j)