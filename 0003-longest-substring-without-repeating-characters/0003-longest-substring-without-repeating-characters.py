class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        left, right = 0, 0
        longest = 0
        for right in range(len(s)):
            while counter.get(s[right]) and counter[s[right]] > 0:
                counter[s[left]] -= 1
                left += 1
            counter[s[right]] = 1 + counter.get(s[right], 0)
            longest = max(longest, right - left + 1)
        return longest