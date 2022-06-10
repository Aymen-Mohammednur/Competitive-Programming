class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest, p1, p2 = 0, 0, 0
        while p2 < len(s):
            if s[p2] in chars:
                longest = max(longest, p2 - p1)
                while s[p2] in chars:
                    chars.remove(s[p1])
                    p1 += 1
            chars.add(s[p2])
            p2 += 1
        longest = max(longest, p2 - p1)
        return longest