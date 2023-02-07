class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        while True:
            for instruction in instructions:
                if instruction == 'G':
                    x += directions[i][0]
                    y += directions[i][1]
                elif instruction == 'L':
                    i = (i - 1) % 4
                else:
                    i = (i + 1) % 4
            if i == 0:
                return x == 0 and y == 0