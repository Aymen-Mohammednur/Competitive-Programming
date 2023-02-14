class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num = sorted(str(n))
        for i in range(30):
            n = str((2 ** i))
            if sorted(n) == num:
                return True
        return False