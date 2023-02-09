class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(s, curr, start):
            if len(curr) == 4 and start == len(s):
                res.append(".".join(curr))
                return
            if len(curr) > 4:
                return
            for i in range(start, min(start + 3, len(s))):
                if s[start] == '0' and i > start:
                    continue
                if int(s[start:i+1]) <= 255:
                    backtrack(s, curr + [s[start:i+1]], i + 1)
        
        backtrack(s, [], 0)
        return res