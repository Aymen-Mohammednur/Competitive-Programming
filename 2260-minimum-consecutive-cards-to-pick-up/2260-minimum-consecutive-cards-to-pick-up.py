class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = defaultdict(int)
        l = 0
        ans = float('inf')
        for r in range(len(cards)):
            while count[cards[r]] != 0:
                ans = min(ans, r - l + 1)
                count[cards[l]] -= 1
                l += 1
            count[cards[r]] += 1
        return ans if ans != float('inf') else -1