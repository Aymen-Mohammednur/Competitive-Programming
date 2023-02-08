class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        counter = Counter(nums)
        if len(counter) < 3:
            return max(counter.keys())
        count = 1
        for num in sorted(counter.keys(), reverse=True):
            if count == 3:
                return num
            count += 1