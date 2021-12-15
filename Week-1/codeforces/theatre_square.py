# https://codeforces.com/problemset/problem/1/A

import math
def theatre_square():
    m, n, a = map(int, input().split())
    print(math.ceil(m / a) * math.ceil(n / a))

theatre_square()