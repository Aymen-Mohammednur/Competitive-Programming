class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        output = []
        while a or b:
            if len(output) >= 2 and output[-1] == output[-2] == 'a':
                output.append('b')
                b -= 1
            elif len(output) >= 2 and output[-1] == output[-2] == 'b':
                output.append('a')
                a -= 1
            if a and a > b:
                output.append('a')
                a -= 1
            elif b and b >= a:
                output.append('b')
                b -= 1
        return "".join(output)