class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = 0
        for even in range(len(nums)):
            if nums[even] % 2 == 0:
                nums[even], nums[odd] = nums[odd], nums[even]
                odd += 1
        return nums