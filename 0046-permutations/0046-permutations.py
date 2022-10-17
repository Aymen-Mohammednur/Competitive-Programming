class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def backtrack(counter, curr):
            if len(curr) == len(nums):
                permutations.append(curr.copy())
            for num in counter:
                if counter[num] > 0:
                    curr.append(num)
                    counter[num] -= 1
                    backtrack(counter, curr)
                    counter[num] += 1
                    curr.pop()
        backtrack(Counter(nums), [])
        return permutations