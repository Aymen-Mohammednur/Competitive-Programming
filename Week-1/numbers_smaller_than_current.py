# LEETCODE 1365
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smallerNumbersThanCurrent(nums):
    countArr = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[j] < nums[i]):
                countArr[i] += 1
    return countArr