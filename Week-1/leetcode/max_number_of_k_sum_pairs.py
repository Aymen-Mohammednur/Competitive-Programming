# LEETCODE 1679
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

from collections import defaultdict
from typing import Counter, List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # counter = Counter(nums)
        # count = 0
        # for i in sorted(counter.keys()):
        #     while(counter[i] and counter[k-i] and counter[i] + counter[k-1] > 1):
        #         count += 1
        #         counter[i] -= 1
        #         counter[k-i] -= 1
        #         # print(count)
        # return count

        count = 0
        Dict = defaultdict(int)
        for i in range(len(nums)):
            if (k - nums[i] not in Dict):
                Dict[nums[i]] += 1
            else:
                Dict[k - nums[i]] -= 1
                if Dict[k - nums[i]] == 0:
                    Dict.pop(k - nums[i])
                count += 1
            print(Dict)
        return count


nums = [1, 4, 4, 2, 2, 2]
k = 6
print(Solution().maxOperations(nums, k))
