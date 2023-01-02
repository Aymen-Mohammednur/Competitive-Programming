class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        mapping = {}
        used = set()
        for i in range(len(s)):
            if mapping.get(pattern[i]):
                if s[i] != mapping.get(pattern[i]):
                    return False
            else:
                if s[i] not in used:
                    mapping[pattern[i]] = s[i]
                    used.add(s[i])
                else:
                    return False
        return True