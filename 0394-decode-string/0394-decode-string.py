class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                string = ""
                while stack and stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                num = ''
                while stack and '0' <= stack[-1] <= '9':
                    num = stack.pop() + num
                stack.append(string * int(num))
        return ''.join(stack)