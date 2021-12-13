# LEETCODE
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = int)
        return nums[-k]