class Solution:
    def flip(self, arr, k):
        left = 0
        while left <= k:
            arr[left], arr[k] = arr[k], arr[left]
            left += 1
            k -= 1
        
    def pancakeSort(self, arr: List[int]) -> List[int]:
        seq = []
        _max = max(arr)
        flip_until = len(arr) - 1
        while _max > 1:
            max_index = arr.index(_max)
            self.flip(arr, max_index)
            self.flip(arr, flip_until)
            seq.append(max_index + 1)
            seq.append(flip_until + 1)
            _max -= 1
            flip_until -= 1
        return seq