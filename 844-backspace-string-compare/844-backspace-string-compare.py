class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for c in s:
            if not stack1 and c == "#":
                continue
            if stack1 and c == '#':
                stack1.pop()
            else:
                stack1.append(c)
        stack2 = []
        for c in t:
            if not stack2 and c == "#":
                continue
            if stack2 and c == '#':
                stack2.pop()
            else:
                stack2.append(c)
        return stack1 == stack2