class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = list(street)
        count = 0
        for i in range(len(street)):
            if street[i] == 'H':
                if i > 0 and street[i - 1] == 'B':
                    continue
                if i < len(street) - 1 and street[i + 1] == '.':
                    street[i + 1] = 'B'
                    count += 1
                elif i > 0 and street[i - 1] == '.':
                    street[i - 1] = 'B'
                    count += 1
                else:
                    return -1
        return count