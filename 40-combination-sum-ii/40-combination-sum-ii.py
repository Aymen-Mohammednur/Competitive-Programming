class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        candidates.sort()
        def backtrack(combo, currSum, start):
            if currSum > target:
                return
            if currSum == target:
                combos.append(combo.copy())
                return
            prev = None
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue 
                currSum += candidates[i]
                prev = candidates[i]
                combo.append(candidates[i])
                backtrack(combo, currSum, i + 1)
                currSum -= combo.pop()
        backtrack([], 0, 0)
        return combos