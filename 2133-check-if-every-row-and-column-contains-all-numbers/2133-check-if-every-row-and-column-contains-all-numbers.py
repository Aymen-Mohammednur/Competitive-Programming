class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            row, col = set(), set()
            for j in range(len(matrix[0])):
                row.add(matrix[i][j])
                col.add(matrix[j][i])
            if len(row) != len(matrix) or len(col) != len(matrix):
                return False
        return True