class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = float('-inf')
        counter = Counter(arr)
        for n, f in counter.items():
            if n == f:
                res = max(res, n)
        return res if res != float('-inf') else -1