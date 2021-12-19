# LEETCODE 1190
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        queue = deque()
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                while stack and stack[-1] != "(" and i == ")":
                    queue.append(stack.pop())
                if stack[-1] =="(" and i == ")":
                    stack.pop()
                while len(queue) > 0:
                    stack.append(queue.popleft())
        return "".join(stack)


s = "(u(love)i)"
print(Solution().reverseParentheses(s))
