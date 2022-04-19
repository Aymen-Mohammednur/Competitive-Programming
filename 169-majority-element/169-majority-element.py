class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums)
        for i in range(len(nums)):
            if counter[nums[i]] > n / 2:
                return nums[i]