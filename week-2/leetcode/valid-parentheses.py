# LEETCODE 20
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Dict = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if (s[i] in Dict):
                if stack and stack[-1] == Dict[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        if (len(stack) == 0):
            return True