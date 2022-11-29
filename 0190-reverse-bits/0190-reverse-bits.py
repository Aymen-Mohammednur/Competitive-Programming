class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = []
        for i in range(32):
            if n & (1 << i):
                reverse.append('1')
            else:
                reverse.append('0')
        return int(''.join(reverse), 2)