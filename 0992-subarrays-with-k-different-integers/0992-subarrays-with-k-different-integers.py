class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def window(nums, k):
            l, r = 0, 0
            res = 0
            seen = set()
            counter = Counter()
            while r < len(nums):
                seen.add(nums[r])
                counter[nums[r]] += 1
                while len(seen) > k:
                    counter[nums[l]] -= 1
                    if counter[nums[l]] == 0:
                        seen.remove(nums[l])
                    l += 1
                res += (r - l + 1)
                r += 1
            return res
        
        return window(nums, k) - window(nums, k - 1)