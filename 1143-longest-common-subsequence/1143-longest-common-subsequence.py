class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # bottom-up
#         dp = [[0 for i in range(len(text2))] for j in range(len(text1))]
#         for i in range(len(text1)):
#             for j in range(len(text2)):
#                 if text1[i] == text2[j]:
#                     print(text1[i], text2[j])
#                     dp[i][j] = 1 + (dp[i - 1][j - 1] if i and j else 0)
#                 else:
#                     dp[i][j] = max(dp[i][j - 1] if j else 0, dp[i - 1][j] if i else 0)
#         print(dp)
#         return dp[-1][-1]
        
        # def dp(i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if (i, j) in memo:
        #         return memo[i, j]
        #     if text1[i] == text2[j]:
        #         memo[i, j] = 1  + dp(i-1, j-1)
        #     else:
        #         memo[i,j] = max(dp(i-1, j), dp(i, j-1))
        #     return memo[i, j]
        
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        # for i, j in product(range(m), range(n)):
        #     dp[i][j][1] = 1
        
        for i, j in product(range(1, m+1), range(1,n+1)):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1  + dp[i-1][j-1] 
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n] 
        
    
    
        # top-down
        # memo = {}
        # def top_down(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     longest = 0
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     if text1[i] == text2[j]:
        #         longest = 1 + top_down(i + 1, j + 1)
        #     else:
        #         longest = max(top_down(i, j + 1), top_down(i + 1, j))
        #     memo[(i, j)] = longest
        #     return longest
        # return top_down(0, 0)