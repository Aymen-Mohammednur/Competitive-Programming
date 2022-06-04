class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colsUsed = set()
        positiveDiag = set()
        negativeDiag = set()
        output = []
        ans = [["."] * n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                output.append(["".join(r) for r in ans])
                return
            
            for c in range(n):
                if c in colsUsed or (r + c) in positiveDiag or (r - c) in negativeDiag:
                    continue
                    
                colsUsed.add(c)
                positiveDiag.add(r + c)
                negativeDiag.add(r - c)
                ans[r][c] = "Q"
                
                backtrack(r + 1)
                
                colsUsed.remove(c)
                positiveDiag.remove(r + c)
                negativeDiag.remove(r - c)
                ans[r][c] = "."
                
        backtrack(0)
        return output