class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue = deque()
        for d in deck:
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(d)
        return list(queue)