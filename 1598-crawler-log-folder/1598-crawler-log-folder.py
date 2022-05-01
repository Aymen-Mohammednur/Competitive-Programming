class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "./":
                continue
            elif log != "../":
                stack.append(log)
            elif stack:
                stack.pop()
        return len(stack)