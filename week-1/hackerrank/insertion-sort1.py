# https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    # Write your code here
    val = arr[-1]
    for i in range(n - 2, -1, -1):
        if (arr[i] > val):
            arr[i + 1] = arr[i]
            print(*arr)
        if (i == 0):
            arr[i] = val
            print(*arr)
        elif (arr[i] < val):
            arr[i + 1] = val
            print(*arr)
            break


print(insertionSort1(5, [1, 2, 4, 5, 3]))
