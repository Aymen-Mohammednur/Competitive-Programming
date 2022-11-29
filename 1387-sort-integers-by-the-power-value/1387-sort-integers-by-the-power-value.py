class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1:0}
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 0
            if n % 2 == 0:
                memo[n] = dp(n // 2) + 1
                return memo[n]
            else:
                memo[n] = dp((3 * n) + 1) + 1
                return memo[n]
        power = []
        for i in range(lo, hi + 1):
            power.append(i)
            dp(i)
        power.sort(key = lambda x: memo[x])
        return power[k - 1]