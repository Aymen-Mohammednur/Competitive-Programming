class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new = [0] * len(arr)
        offset = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                offset += 1
            else:
                if i + offset < len(arr):
                    new[i + offset] = arr[i]
            arr[i] = new[i]
        