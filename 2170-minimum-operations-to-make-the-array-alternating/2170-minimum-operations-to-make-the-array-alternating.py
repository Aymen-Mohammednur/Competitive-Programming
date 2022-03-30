class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        evenCount = defaultdict(int)
        oddCount = defaultdict(int)
        for i in range(0, len(nums), 2):
            evenCount[nums[i]] += 1
        for i in range(1, len(nums), 2):
            oddCount[nums[i]] += 1
            ''
        evenCount[-1] = 0
        oddCount[-1] = 0
        evenCount = sorted(evenCount.items(), key = lambda x:x[1], reverse = True)
        oddCount = sorted(oddCount.items(), key = lambda x:x[1], reverse = True)

        if evenCount[0][0] == oddCount[0][0]:
            temp1 = evenCount[0][1] + oddCount[1][1]
            temp2 = evenCount[1][1] + oddCount[0][1]
            return len(nums) - max(temp1, temp2)

        return len(nums) - (evenCount[0][1] + oddCount[0][1])