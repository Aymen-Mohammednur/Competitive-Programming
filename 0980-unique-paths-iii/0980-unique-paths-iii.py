class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        obstacles = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    starting = (i,j)
                if grid[i][j] == 2:
                    ending = (i,j)
                if grid[i][j] == -1:
                    obstacles += 1
        pathLength = (len(grid) * len(grid[0])) - obstacles
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        count = 0
        visited = set()
        def isValid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != -1
        def dfs(i, j):
            nonlocal count
            visited.add((i,j))
            if len(visited) == pathLength and (i,j) == ending:
                count += 1
                # return
            for x, y in directions:
                if isValid(x + i, y + j) and (i + x, j + y) not in visited:
                    dfs(x + i, y + j)
            visited.remove((i,j))
        dfs(starting[0], starting[1])
        return count