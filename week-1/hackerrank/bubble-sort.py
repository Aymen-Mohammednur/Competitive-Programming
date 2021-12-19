# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def countSwaps(a):
    # Write your code here
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    print("Array is sorted in {0} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
