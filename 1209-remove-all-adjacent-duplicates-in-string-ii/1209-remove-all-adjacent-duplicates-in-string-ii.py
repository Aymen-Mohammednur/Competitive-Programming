class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            if stack[-1][1] == k:
                stack.pop()
        output = []
        for i in range(len(stack)):
            output.append(stack[i][0] * stack[i][1])
        return "".join(output)