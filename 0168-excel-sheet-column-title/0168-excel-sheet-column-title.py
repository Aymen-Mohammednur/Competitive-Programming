class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ''
        while columnNumber:
            columnNumber -= 1
            res = letters[columnNumber % 26] + res
            columnNumber //= 26
        return res