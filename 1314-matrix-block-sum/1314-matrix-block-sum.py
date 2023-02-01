class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        1 2 3
        4 5 6
        7 8 9
        
        0,0 - 0,0 : 1
        0,0 - 0,1 : 3
        0,0 - 0,2 : 6
        
        
        1  3  6
        5  12 21
        12 27 45
        
        0,0 0,1 1,0 1,1
        0,2 => 0,1 0,2 1,1, 1,2
        
        """
        m, n = len(mat), len(mat[0])
        def helper(i, j):
            rows, cols = [], []
            min_row = max(0, i-k)
            max_row = min(m, i+k+1)
            for r in range(min_row, max_row):
                rows.append(r)
            min_col = max(0, j-k)
            max_col = min(n, j+k+1)
            for c in range(min_col, max_col):
                cols.append(c)
            return [rows, cols]
                
        output = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rows, cols = helper(i, j)
                _sum = 0
                for r in rows:
                    for c in cols:
                        _sum += mat[r][c]
                output[i][j] = _sum
        return output