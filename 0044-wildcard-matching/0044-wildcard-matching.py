class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            if i < len(s) and (s[i] == p[j] or p[j] == '?'):
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            if p[j] == '*':
                memo[(i, j)] = dfs(i, j + 1) or (i < len(s) and dfs(i + 1, j))
                return memo[(i, j)]
            
            return False
        
        return dfs(0, 0)