class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        for i in range(n.bit_length()):
            n ^= (1 << i)
        return n