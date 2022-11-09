class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = set()
        ans = []
        for num in nums:
            if num in duplicate:
                ans.append(num)
            duplicate.add(num)
        for i in range(1, len(nums) + 1):
            if i not in duplicate:
                ans.append(i)
                return ans