class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n
        p1 = m
        p2 = 0
        while p1 < l and p2 < n:
            nums1[p1] = nums2[p2]
            p1 += 1
            p2 += 1
        nums1.sort()