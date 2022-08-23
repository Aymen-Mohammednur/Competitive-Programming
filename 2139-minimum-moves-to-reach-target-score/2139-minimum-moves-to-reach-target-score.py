class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            while maxDoubles and target % 2 == 0:
                target //= 2
                maxDoubles -= 1
                moves += 1
            if target > 1:
                target -= 1
                moves += 1
            if not maxDoubles:
                moves += target - 1
                break
        return moves
                