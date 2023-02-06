class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if len(pref) <= len(word) and word[:len(pref)] == pref:
                count += 1
        return count