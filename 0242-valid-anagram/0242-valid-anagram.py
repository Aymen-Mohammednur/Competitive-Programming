class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        store1 = {}
        store2 = {}
        for char1, char2 in zip(s, t):
            store1[char1] = store1.get(char1, 0) + 1
            store2[char2] = store2.get(char2, 0) + 1
        return store1 == store2