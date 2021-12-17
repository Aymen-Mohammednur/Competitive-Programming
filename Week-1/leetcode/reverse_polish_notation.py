# LEETCODE 150
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List
import re

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            print(stack)
            if (re.match("[-+]?\d+$", tokens[i]) is not None):
                stack.append(tokens[i])
            elif (stack and re.match("[-+]?\d+$", tokens[i]) is None):
                temp1 = str(stack.pop())
                temp2 = str(stack.pop())
                stack.append(int(eval(temp2+tokens[i]+temp1)))
        return stack.pop()


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(tokens))
