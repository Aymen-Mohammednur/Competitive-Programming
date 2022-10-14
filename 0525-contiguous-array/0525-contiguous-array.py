class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapping = { 0: -1 }
        count = 0
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in mapping:
                maxLen = max(maxLen, i - mapping[count])
            else:
                mapping[count] = i
        return maxLen