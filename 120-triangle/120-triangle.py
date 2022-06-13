class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def compute(level, index):
            if memo.get((level, index)) is not None:
                return memo[(level, index)]
            if level == len(triangle) - 1:
                memo[(level, index)] = triangle[level][index]
                return memo[(level, index)]
            left = compute(level + 1, index)
            right = compute(level + 1, index + 1)
            memo[(level, index)] = min(left, right) + triangle[level][index]
            return memo[(level, index)]
        return compute(0, 0)
    