class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        counter = 0
        stop = 2
        for i in range(1, n + 1):
            if i == stop:
                stop *= 2
                counter = 0
            result.append(result[counter] + 1)
            counter += 1
        return result