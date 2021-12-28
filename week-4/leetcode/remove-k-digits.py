# LEETCODE 402
# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        monoStack = []
        count = 0
        nums = [n for n in num]
        if len(nums) == k:
            return "0"
        for i in nums:
            while monoStack and monoStack[-1] > i and count < k:
                monoStack.pop()
                count += 1
            monoStack.append(i)
        while count != k:
            monoStack.pop()
            count += 1
        return str(int("".join(monoStack)))