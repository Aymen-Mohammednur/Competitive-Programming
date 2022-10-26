class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        while fib[-1] + fib[-2] <= k:
            fib.append(fib[-1] + fib[-2])
        s = 0
        i = len(fib) - 1
        target = k
        count = 0
        while s != k and i >= 0:
            if fib[i] <= target:
                count += 1
                s += fib[i]
                target -= fib[i]
            i -= 1
        return count
            