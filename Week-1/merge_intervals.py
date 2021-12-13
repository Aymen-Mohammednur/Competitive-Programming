def merge(intervals):
    output = []
    j = 0
    while (j < len(intervals) - 1):
        print(j)
        # print(intervals[i])
        if (intervals[j][1] >= intervals[j+1][0]):
            output.append([intervals[j][0], intervals[j+1][1]])
            j += 2
            # print(i)
            # del intervals[i:i+2]
            # intervals.remove(intervals[i])
            # intervals.remove(intervals[i])
        else:
            output.append(intervals[j])
            j += 1
    return output


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
