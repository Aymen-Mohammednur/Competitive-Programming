import math

def domino_piling(m, n):
    temp = m * n
    return math.floor(temp / 2)

print(domino_piling(1, 1))
