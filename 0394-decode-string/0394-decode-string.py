class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                string = []
                while stack and stack[-1] != '[':
                    string.append(stack.pop())
                stack.pop()
                string.reverse()
                new_str = ''.join(string)
                num = ''
                while stack and '0' <= stack[-1] <= '9':
                    num = stack.pop() + num
                for _ in range(int(num)):
                    stack.append(new_str)
        return ''.join(stack)