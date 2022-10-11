class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            target = 0 - nums[i]
            difference = {}
            for j in range(i + 1, len(nums)):
                if nums[j] in difference:
                    triplets = (nums[i], nums[difference[nums[j]]], nums[j])
                    t = tuple(sorted(triplets))  
                    result.add(t)
                difference[target- nums[j]] = j
        return result