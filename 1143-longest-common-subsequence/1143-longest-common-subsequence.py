class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def top_down(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            longest = 0
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                longest = 1 + top_down(i + 1, j + 1)
            else:
                longest = max(top_down(i, j + 1), top_down(i + 1, j))
            memo[(i, j)] = longest
            return longest
        return top_down(0, 0)