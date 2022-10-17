class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def backtrack(curr):
            if len(curr) == len(nums):
                permutations.append(curr.copy())
            for i in range(len(nums)):
                if nums[i] in curr:
                    continue
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
        backtrack([])
        return permutations