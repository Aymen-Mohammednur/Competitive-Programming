class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        directions = [up, down. left right]
        visited
        dfs(index, currSum):
            add to visited
            currSum += index
            ans= max(ans, currSUm)
            for all directions:
                if not visited:
                    dfs(index + direction, currSum))
            return ans
        for each position:
            max(ans, dfs)
        """
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        def isValid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 0
        
        ans = 0
        def dfs(i, j, currSum):
            nonlocal ans
            visited.add((i, j))
            currSum += grid[i][j]
            ans = max(ans, currSum)
            for x, y in directions:
                if isValid(x + i, y + j) and (x + i, y + j) not in visited:
                    dfs(x + i, y + j, currSum)
            visited.remove((i, j))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    visited = set()
                    dfs(i, j, 0)
        
        return ans