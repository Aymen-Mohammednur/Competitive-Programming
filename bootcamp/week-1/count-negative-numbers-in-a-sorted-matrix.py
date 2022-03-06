# LEETCODE 1351

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for grid in grid:
            left = 0
            right = len(grid) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if grid[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            count += len(grid) - left
        return count