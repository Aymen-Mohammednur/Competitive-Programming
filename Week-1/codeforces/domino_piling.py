# https://codeforces.com/problemset/problem/50/A

import math

def domino_piling():
    inp = input()
    lst = inp.split(" ")
    m, n = int(lst[0]), int(lst[1])
    temp = m * n
    return math.floor(temp / 2)
        
print(domino_piling())
