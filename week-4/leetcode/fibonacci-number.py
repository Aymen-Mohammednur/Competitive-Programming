# LEETCODE 509
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def __init__(self):
        self.mem = [0] * 31
    def fib(self, n: int) -> int:
        if self.mem[n]:
            return self.mem[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        self.mem[n-1] = self.fib(n-1)
        self.mem[n-2] = self.fib(n-2)
        return self.mem[n-1] + self.mem[n-2]