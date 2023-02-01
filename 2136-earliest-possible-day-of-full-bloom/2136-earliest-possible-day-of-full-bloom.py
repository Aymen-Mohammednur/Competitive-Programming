class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant_grow = []
        for i in range(len(plantTime)):
            plant_grow.append((growTime[i], plantTime[i]))
        plant_grow.sort()
        res = 0
        for grow_time, plant_time in plant_grow:
            res = max(res, grow_time) + plant_time
        return res