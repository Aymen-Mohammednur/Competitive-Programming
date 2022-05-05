class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        sub = 0
        for char in t:
            if sub < len(s):
                if char == s[sub]:
                    sub += 1
        return sub == len(s)