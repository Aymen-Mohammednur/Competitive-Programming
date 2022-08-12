class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        def isValid(i, j):
            return 0 <= i < row and 0 <= j < col and grid[i][j] == 1
        perimeter = 0
        def dfs(row, col):
            nonlocal perimeter
            visited.add((row, col))
            for x, y in directions:
                if not isValid(row + x, col + y) and (row + x, col + y) not in visited:
                    perimeter += 1
                    continue
                if isValid(row + x, col + y) and (row + x, col + y) not in visited:
                    dfs(row + x, col + y)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j)
        return perimeter