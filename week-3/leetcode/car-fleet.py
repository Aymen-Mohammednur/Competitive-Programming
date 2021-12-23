# LEETCODE 853
# https://leetcode.com/problems/car-fleet/

from typing import List

class Solution:
    def helper(self, target, positionSpeed):
        return (target - positionSpeed[0]) / positionSpeed[1]

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        positionSpeed = []
        fleets = 1
        for i in range(len(position)):
            positionSpeed.append([position[i], speed[i]])
        positionSpeed.sort()

        time = self.helper(target, positionSpeed[-1])
        for i in range(len(positionSpeed) - 2, -1, -1):
            if self.helper(target, positionSpeed[i]) <= time:
                continue
            elif self.helper(target, positionSpeed[i]) > time:
                time = self.helper(target, positionSpeed[i])
                fleets += 1
        return fleets


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

# target = 10
# position = [0, 4, 2]
# speed = [2, 1, 3]
print(Solution().carFleet(target, position, speed))
# print(Solution().helper(10, [0, 1]))
