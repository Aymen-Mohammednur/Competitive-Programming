class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        neg = num < 0
        num = abs(num)
        stack = []
        while num:
            stack.append(str(num % 7))
            num = num // 7
        res = ''
        while stack:
            res += stack.pop()
        if neg:
            return '-' + res
        return res