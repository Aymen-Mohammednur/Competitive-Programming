class UnionFind:
    def __init__(self, n, m, grid):
        self.root = [[(i,j) for j in range(m)] for i in range(n)]
        self.size = deepcopy(grid)
        self.n, self.m = n, m
        
    def find(self, i, j):
        if self.root[i][j] == (i, j):
            return (i, j)
        self.root[i][j] = self.find(self.root[i][j][0], self.root[i][j][1])
        return self.root[i][j]
    
    def union(self, i1, j1, i2, j2):
        rootA = self.find(i1, j1)
        rootB = self.find(i2, j2)
        if rootA != rootB:
            i1A, j1A = rootA
            i1B, j1B = rootB
            if self.size[i1A][j1A] > self.size[i1B][j1B]:
                self.root[i1B][j1B] = rootA
                self.size[i1A][j1A] += self.size[i1B][j1B]
            else:
                self.root[i1A][j1A] = rootB
                self.size[i1B][j1B] += self.size[i1A][j1A]
    
    def getArea(self):
        area = 0
        for i in range(self.n):
            for j in range(self.m):
                area = max(area, self.size[i][j])
        return area

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        disjoint = UnionFind(len(grid), len(grid[0]), grid)
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def inBound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for x, y in directions:
                        if inBound(x + i, y + j) and grid[x + i][y + j] == 1:
                            disjoint.union(i, j, x + i, y + j)
        return disjoint.getArea()