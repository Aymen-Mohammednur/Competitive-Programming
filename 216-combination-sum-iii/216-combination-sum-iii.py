class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs = []
        def backtrack(comb, currSum, start):
            if currSum == n and len(comb) == k:
                combs.append(comb.copy())
            for i in range(start, 10):
                comb.append(i)
                currSum += i
                backtrack(comb, currSum, i + 1)
                currSum -= comb.pop()
        backtrack([], 0, 1)
        return combs
                