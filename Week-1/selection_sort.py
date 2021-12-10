class Solution: 
    def select(self, arr, i):
        min_index = i
        for j in range(i, len(arr)):
            if (arr[min_index] > arr[j]):
                min_index = j
        return min_index
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_index = self.select(arr, i)
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr
        
sol = Solution()
arr = [3, 1, 5, 2, 4]
arr2 = [64, 25, 12, 22, 11]
print(sol.selectionSort(arr2, 5))
