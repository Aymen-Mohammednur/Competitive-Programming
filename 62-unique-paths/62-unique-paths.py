class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n and (i, j) not in visited
        directions = [(0,1), (1,0)]
        visited = set()
        
        @lru_cache(None)
        def dfs(i, j):
            count = 0
            if (i, j) == (m-1, n-1):
                return 1
            for x, y in directions:
                if isValid(i + x, j + y):
                    count += dfs(i + x, j + y)
            return count
        return dfs(0, 0)