class Solution:
    def longestPrefix(self, s: str) -> str:
        LPS = [0] * len(s)
        i = 0
        for j in range(1, len(s)):
            while s[i] != s[j] and i != 0:
                i = LPS[i - 1]
            if s[i] == s[j]:
                LPS[j] = i + 1
                i += 1
        return s[:LPS[-1]]