class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        mapping = defaultdict(str)
        count = defaultdict(int)
        for i in range(len(pattern)):
            if mapping[pattern[i]]:
                if mapping[pattern[i]] != s[i]:
                    return False
            else:
                if count[s[i]] > 0:
                    return False
                mapping[pattern[i]] = s[i]
                count[s[i]] += 1
        return True