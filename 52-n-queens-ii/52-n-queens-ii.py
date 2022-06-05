class Solution:
    def totalNQueens(self, n: int) -> int:
        colsUsed = set()
        pDiag = set()
        nDiag = set()
        count = 0
        
        def dfs(r):
            nonlocal count
            if r == n:
                count += 1
                return
            
            for c in range(n):
                if c in colsUsed or (r + c) in pDiag or (r - c) in nDiag:
                    continue
                    
                colsUsed.add(c)
                pDiag.add(r + c)
                nDiag.add(r - c)
                
                dfs(r + 1)
                
                colsUsed.remove(c)
                pDiag.remove(r + c)
                nDiag.remove(r - c)
        
        dfs(0)
        return count