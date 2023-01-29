class Solution:
    def romanToInt(self, s: str) -> int:
        store = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        prev = 0
        for i in range(len(s) - 1, -1, -1):
            if store[s[i]] >= prev:
                res += store[s[i]]
            else:
                res -= store[s[i]]
            prev = store[s[i]]
        return res