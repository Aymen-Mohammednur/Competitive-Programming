class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        res = 0
        for char in t:
            if s_counter[char] > 0:
                s_counter[char] -= 1
            else:
                res += 1
        return res