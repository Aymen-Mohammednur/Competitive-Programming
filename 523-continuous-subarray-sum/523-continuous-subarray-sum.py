class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mapping = {0 : -1}
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            rem = currSum % k
            if rem in mapping:
                if i - mapping[rem] >= 2:
                    return True
            else:
                mapping[rem] = i
        return False