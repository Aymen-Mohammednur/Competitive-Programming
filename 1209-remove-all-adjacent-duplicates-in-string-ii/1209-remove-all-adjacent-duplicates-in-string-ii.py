class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["0", 0]]
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        output = []
        for i in range(1, len(stack)):
            output.append(stack[i][0] * stack[i][1])
        return "".join(output)