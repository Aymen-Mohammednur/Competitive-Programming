# LEETCODE 1365
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smallerNumbersThanCurrent(nums):
    countArr = [0 for i in range(101)]
    for i in range(len(nums)):
        countArr[nums[i]] += 1

    for i in range(1, len(countArr)):
        countArr[i] += countArr[i - 1]
    print(countArr)
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = countArr[nums[i]]
        else:
            print(nums[i])
            nums[i] = countArr[nums[i] - 1]

    return nums


arr = [6, 5, 4, 8]
print(smallerNumbersThanCurrent(arr))
