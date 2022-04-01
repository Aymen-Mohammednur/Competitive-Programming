class Solution:
    def fib(self, n: int) -> int:
        # memo = {0 : 0, 1: 1}
        @cache
        def compute(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            # if n in memo:
            #     return memo[n]
            # memo[n] = compute(n-1) + compute(n-2)
            return compute(n-1) + compute(n-2)
        return compute(n)