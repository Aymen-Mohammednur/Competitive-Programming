class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        for _ in range(num.bit_length()):
            num ^= i
            i = i << 1
        return num