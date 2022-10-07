class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        def backtrack(combo, currSum, start):
            if currSum > target:
                return
            if currSum == target:
                combos.append(combo.copy())
                return
            for i in range(start, len(candidates)):
                currSum += candidates[i]
                combo.append(candidates[i])
                backtrack(combo, currSum, i)
                currSum -= combo.pop()
        backtrack([], 0, 0)
        return combos