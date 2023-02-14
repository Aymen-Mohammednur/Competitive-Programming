class Solution:
    def sumZero(self, n: int) -> List[int]:
        _n = n
        if n % 2 != 0:
            _n -= 1
        res = []
        for i in range(1, (_n // 2) + 1):
            res.append(i)
            res.append(-i)
        if n % 2 != 0:
            res.append(0)
        return res