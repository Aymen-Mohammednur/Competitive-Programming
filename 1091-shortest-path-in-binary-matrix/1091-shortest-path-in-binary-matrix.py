class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        queue = deque([(0, 0, 1)])
        directions = [(1,1), (1,0), (0,1), (0,-1), (-1,0), (-1,-1), (-1,1), (1,-1)]
        visited = set()
        def isValid(i, j):
            return 0 <= i < n and 0 <= j < n and (i, j) not in visited and grid[i][j] == 0
        result = float('inf')
        while queue:
            (i, j, path) = queue.popleft()
            visited.add((i, j))
            if (i, j) == (n - 1, n - 1):
                result = path
                break
            for x, y in directions:
                if isValid(x + i, y + j) and grid[x + i][y + j] == 0:
                    queue.append((x + i, y + j, path + 1))
                    grid[x + i][y + j] = 2
        return result if result != float('inf') else -1