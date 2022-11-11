class Solution:
    def calcArea(self, a, b, c):
        semi_perimeter = (a + b + c) / 2
        temp = semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)
        return math.sqrt(temp) if temp > 0 else 0
    
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(2, len(nums)):
            if self.calcArea(nums[i], nums[i-1], nums[i-2]) != 0.0:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0