class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        def inBound(r, c):
            return 0 <= r < n and 0 <= c < m
        def dfs(r, c):
            visited.add((r,c))
            for x, y in directions:
                nr, nc = x+r, y+c
                if inBound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == '1':
                    dfs(nr, nc)
        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    count += 1
        return count