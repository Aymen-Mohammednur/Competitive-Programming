def countingSort(arr):
    # Write your code here
    countArr = [0] * 100
    for i in range(len(arr)):
        countArr[arr[i]] += 1

    count = 0
    for i in range(len(countArr)):
        if (countArr[i] == 0):
            continue
        for j in range(countArr[i]):
            arr[count] = i
            count += 1

    return arr


arr = [8, 1, 2, 2, 3]
print(countingSort(arr))
