class Solution:
    def inBound(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.m
    
    def dfs(self, row, col, ocean, heights):
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ocean.add((row, col))
        for x, y in directions:
            nr, nc = x+row, y+col
            if self.inBound(nr, nc) and (nr, nc) not in ocean and heights[row][col] <= heights[nr][nc]:
                self.dfs(nr, nc, ocean, heights)
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.n, self.m = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        for row in range(self.n):
            self.dfs(row, 0, pacific, heights)
            self.dfs(row, self.m - 1, atlantic, heights)
            
        for col in range(self.m):
            self.dfs(0, col, pacific, heights)
            self.dfs(self.n - 1, col, atlantic, heights)
        
        res = []
        for i in range(self.n):
            for j in range(self.m):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res