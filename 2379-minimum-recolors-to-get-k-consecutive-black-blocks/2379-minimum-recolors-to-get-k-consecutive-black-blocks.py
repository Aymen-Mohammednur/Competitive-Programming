class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 0
        count = 0
        for i in range(k):
            if blocks[i] == 'B':
                count += 1
        res = count
        l = 0
        for r in range(k, len(blocks)):
            if blocks[l] == 'B':
                count -= 1
            if blocks[r] == 'B':
                count += 1
            l += 1
            res = max(res, count)
        return k - res
        