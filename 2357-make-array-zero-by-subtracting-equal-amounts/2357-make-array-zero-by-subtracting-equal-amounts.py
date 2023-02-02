class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return len(counter) - 1 if 0 in counter else len(counter)