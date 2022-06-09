class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 1:
            return n
        one, two, three = 0, 1, 1
        arr = [0, 1, 1]
        for i in range(n - 2):
            arr.append(arr[-1] + arr[-2] + arr[-3])
        return arr[-1]