class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        left = 0
        maxLen = -1
        for right in range(len(s)):
            counter[s[right]] += 1
            window = (right - left) + 1
            if window - max(counter.values()) <= k:
                if window > maxLen:
                    maxLen = window
            else:
                counter[s[left]] -= 1
                left += 1
        return maxLen