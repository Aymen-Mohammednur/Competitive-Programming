class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        i = 0
        while tickets[k] != 0:
            if i >= len(tickets):
                i = 0
            if tickets[i] == 0:
                i += 1
                continue
            tickets[i] -= 1
            time += 1
            i += 1
        return time