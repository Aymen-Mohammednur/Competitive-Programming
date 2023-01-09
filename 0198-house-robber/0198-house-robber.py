class Solution:
    def rob(self, nums: List[int]):
        '''
        return which houses you robbed
        '''
        prev1 = 0
        prev2 = 0
        for n in nums:
            tmp = prev1
            prev1 = max(prev1, prev2 + n)
            prev2 = tmp
        return prev1
        