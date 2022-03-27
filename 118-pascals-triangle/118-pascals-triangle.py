class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for i in range(1, numRows):
            new = [1]
            for j in range(i - 1):
                new.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            new.append(1)
            pascal.append(new)
        return pascal