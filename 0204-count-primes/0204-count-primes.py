class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [i for i in range(n)]
        primes = 0
        limit = math.ceil(math.sqrt(n))
        for i in range(2, limit):
            if nums[i] == 0:
                continue
            for j in range(i * i, len(nums), i):
                nums[j] = 0
        for i in range(2, len(nums)):
            if nums[i] != 0:
                primes += 1
        return primes