class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def ones(img):
            res = set()
            for y, row in enumerate(img):
                for x, val in enumerate(row):
                    if val == 1:
                        res.add((x, y))
            return res
        
        img1_ones = ones(img1)
        img2_ones = ones(img2)
        store = defaultdict(int)
        for x1, y1 in img1_ones:
            for x2, y2 in img2_ones:
                store[(x1-x2, y1-y2)] += 1
        
        res = 0
        if store:
            res = max(store.values())
        return res