class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1:0}
        def power_value(num):
            if memo.get(num):
                return memo[num]
            if num == 1:
                return 0
            if num % 2 == 0:
                memo[num] = power_value(num / 2) + 1
                return memo[num]
            else:
                memo[num] = power_value((3 * num) + 1) + 1
                return memo[num]
        power = []
        for i in range(lo, hi + 1):
            power.append(i)
            power_value(i)
        power.sort(key=lambda x:memo[x])
        return power[k - 1]