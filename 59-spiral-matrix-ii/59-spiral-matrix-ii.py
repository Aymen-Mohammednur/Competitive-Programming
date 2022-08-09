class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        rowStart = 0
        colStart = 0
        rowEnd = len(matrix) - 1 
        colEnd = len(matrix[0]) - 1
        num = 1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd + 1):
                matrix[rowStart][i] = num
                num += 1
            rowStart += 1
            for i in range(rowStart, rowEnd + 1):
                matrix[i][colEnd] = num
                num += 1
            colEnd -= 1
            if rowStart <= rowEnd:
                for i in range(colEnd, colStart - 1, -1):
                    matrix[rowEnd][i] = num
                    num += 1
                rowEnd -= 1
            if colStart <= colEnd:
                for i in range(rowEnd, rowStart - 1, -1):
                    matrix[i][colStart] = num
                    num += 1
                colStart += 1
        return matrix