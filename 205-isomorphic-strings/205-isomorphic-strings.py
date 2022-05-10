class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = defaultdict(str)
        count = defaultdict(int)
        for i in range(len(s)):
            if mapping[s[i]]:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if count[t[i]] > 0:
                    return False
                mapping[s[i]] = t[i]
                count[t[i]] += 1
        return True