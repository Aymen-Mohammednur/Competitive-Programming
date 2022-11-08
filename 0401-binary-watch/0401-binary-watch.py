class Solution:
    def countSetBits(self, n):
        count = 0
        for i in range(32):
            if n & (1 << i):
                count += 1
        return count
    
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8: return
        result = []
        for hour in range(12):
            for minute in range(60):
                if self.countSetBits(hour) + self.countSetBits(minute) == turnedOn:
                    hr = str(hour)
                    mn = f'{minute:02}'
                    result.append(hr + ':' + mn)
        return result