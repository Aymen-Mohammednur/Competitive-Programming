class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                left = 0
                right = len(matrix[mid]) - 1
                while left <= right:
                    mid2 = (left + right) // 2
                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] < target:
                        left = mid2 + 1
                    else:
                        right = mid2 - 1
                return False
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False