class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * (n + 1)
        for booking in bookings:
            result[booking[0] - 1] += booking[2]
            result[booking[1]] += -booking[2]
        for i in range(1, n):
            result[i] = result[i] + result[i - 1]
        return result[:n]