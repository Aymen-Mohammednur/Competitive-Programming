class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = {}
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                store[s[i]] = i
            elif s[i] in store:
                del store[s[i]]
        if store:
            return min(store.values())
        return -1