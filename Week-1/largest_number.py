from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums)):
            minn = i
            for j in range(i+1, len(nums)):
                # print(nums[minn]+nums[j])
                if (nums[j] + nums[minn] > nums[minn] + nums[j]):
                    minn = j
            nums[i], nums[minn] = nums[minn], nums[i]
        if nums[0] == "0":
            return "0"
        return "".join(nums)