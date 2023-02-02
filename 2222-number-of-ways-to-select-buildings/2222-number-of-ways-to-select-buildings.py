class Solution:
    def numberOfWays(self, s: str) -> int:
        arr = [0, 0, 0, 0, 0, 0] # 0, 1, 01, 10, 010, 101
        for n in s:
            if n == '0':
                arr[0] += 1
                arr[3] += arr[1]
                arr[4] += arr[2]
            else:
                arr[1] += 1
                arr[2] += arr[0]
                arr[5] += arr[3]
        return arr[4] + arr[5]