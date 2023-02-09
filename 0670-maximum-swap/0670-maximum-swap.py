class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        123 321
        """
        res = []
        num = str(num)
        num_list = list(map(str, num))
        for i in range(len(num_list)):
            for j in range(i, len(num_list)):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                temp = ''.join(num_list)
                res.append(int(temp))
                num_list = list(map(str, num))
        if not res:
            return int(num)
        return max(res)