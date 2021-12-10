def countingSort(arr):
    # Write your code here
    countArr = [0] * 100
    for i in range(len(arr)):
        countArr[arr[i]] += 1
    return countArr


arr = [8, 1, 2, 2, 3]
print(countingSort(arr))
