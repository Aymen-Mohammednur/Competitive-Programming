class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        # sort the envelopes based on widths in ascending order
        # if widths are the same, sort based on heights in ascending order
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        dp = [0] * n
        size = 0
        for _, h in envelopes:
            # binary search to find the longest increasing subsequence
            i = bisect.bisect_left(dp, h, 0, size)
            dp[i] = h
            if i == size:
                size += 1
        return size