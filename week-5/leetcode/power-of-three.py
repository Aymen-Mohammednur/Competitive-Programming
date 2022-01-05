# LEETCODE 326
# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 3 or n == 1:
            return True
        if n % 3 != 0 or n < 3:
            return False
        return self.isPowerOfThree(n/3)