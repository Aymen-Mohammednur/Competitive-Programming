class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sr, sc = len(grid) - 1, 0
        count = 0
        while sr >= 0 and sc <= n - 1:
            if grid[sr][sc] < 0:
                count += n - sc
                sr -= 1
            else:
                sc += 1
        return count