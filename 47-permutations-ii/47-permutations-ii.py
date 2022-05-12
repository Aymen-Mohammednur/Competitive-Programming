class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(curr, counter):
            if len(curr) == len(nums):
                temp = curr.copy()
                result.append(temp)
                return
            for num in counter:
                if counter[num] > 0:
                    curr.append(num)
                    counter[num] -= 1
                    dfs(curr, counter)
                    counter[num] += 1
                    curr.pop()
        dfs([], Counter(nums))
        return result