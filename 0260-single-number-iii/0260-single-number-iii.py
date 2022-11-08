class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = x = y = 0
        for n in nums:
            xor ^= n
        
        # to get the first set bit
        bit = 0
        for i in range(32):
            if xor & (1 << i):
                bit = i
                break
        for n in nums:
            if n & (1 << bit):
                y ^= n
        x = xor ^ y
        return [x, y]
