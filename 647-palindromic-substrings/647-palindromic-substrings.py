class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPal(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPal(i, j):
                    count += 1
        return count