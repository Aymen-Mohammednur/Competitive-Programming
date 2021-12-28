# LEETCODE 946
# https://leetcode.com/problems/validate-stack-sequences/

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[pop] and pop < len(popped):
                pop += 1
                stack.pop()
        return len(stack) == 0