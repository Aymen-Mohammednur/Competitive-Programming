class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(curr, idx):
            if idx >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[idx])
            bt(curr, idx + 1)
            curr.pop()
            bt(curr, idx + 1)
        bt([], 0)
        return res