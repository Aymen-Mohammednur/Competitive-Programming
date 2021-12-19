# LEETCODE 969
# https://leetcode.com/problems/pancake-sorting/

from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        Max = len(arr)
        output = []
        while (Max > 0):
            index = arr.index(Max)
            if Max == index + 1:
                Max -= 1
                continue
            arr = arr[index::-1] + arr[index+1:]
            output.append(index+1)
            arr = arr[Max-1::-1] + arr[Max:]
            output.append(Max)
            Max -= 1
        return output


arr = [3, 2, 4, 1]
print(Solution().pancakeSort(arr))
