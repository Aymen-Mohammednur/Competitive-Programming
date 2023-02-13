class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        store[0] = 1
        res = 0
        curr_sum = 0
        for n in nums:
            curr_sum += n
            rem = curr_sum % k
            res += store[rem]
            store[rem] += 1
        return res