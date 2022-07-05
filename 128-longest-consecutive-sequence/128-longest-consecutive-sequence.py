class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        longest = 0
        for num in Set:
            if num - 1 not in Set:
                curr = num
                temp = 1
                while curr + 1 in Set:
                    temp += 1
                    curr = curr + 1
                longest = max(longest, temp)
        return longest