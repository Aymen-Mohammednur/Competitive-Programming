# LEETCODE 1968
# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums


nums = [1, 2, 3, 4, 5]
print(Solution().rearrangeArray(nums))
