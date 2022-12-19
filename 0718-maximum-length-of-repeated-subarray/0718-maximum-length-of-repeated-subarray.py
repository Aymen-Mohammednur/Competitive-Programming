class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums2))] for j in range(len(nums1))]
        _max = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + (dp[i - 1][j - 1] if i and j else 0)
                    _max = max(_max, dp[i][j])
        return _max