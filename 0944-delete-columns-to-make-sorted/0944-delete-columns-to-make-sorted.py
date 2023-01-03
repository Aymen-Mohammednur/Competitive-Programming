class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        grid = []
        for s in strs:
            grid.append(list(s))
        min_cols = 0
        for c in range(len(grid[0])):
            for r in range(1, len(grid)):
                if grid[r][c] < grid[r - 1][c]:
                    min_cols += 1
                    break
        return min_cols