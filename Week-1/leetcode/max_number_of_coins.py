# LEETCODE 1561
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bob = 0
        bobIndex = 0
        me = 0
        alice = 0
        for i in range(len(piles) // 3):
            bob += piles[bobIndex]
            bobIndex += 1
            alice += piles.pop()
            me += piles.pop()
        return me