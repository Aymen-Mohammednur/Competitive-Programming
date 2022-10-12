class Solution:
    def isValid(self, s: str) -> bool:
        closing = { ")":"(", "]":"[", "}":"{" }
        stack = []
        for b in s:
            if not stack and b in closing:
                return False
            if b not in closing:
                stack.append(b)
            elif stack and closing[b] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0