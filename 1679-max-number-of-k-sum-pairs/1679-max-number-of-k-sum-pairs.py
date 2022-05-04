class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        Dict = defaultdict(int)
        for num in nums:
            if Dict[k - num] <= 0:
                Dict[num] += 1
            else:
                Dict[k - num] -= 1
                count += 1
        return count