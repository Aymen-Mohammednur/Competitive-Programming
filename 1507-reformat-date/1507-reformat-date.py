class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        res = []
        date = date.split(' ')
        for i in range(len(date) - 1, -1, -1):
            d = date[i]
            if i == 1:
                d = str(months.index(d)).zfill(2)
            if i == 0:
                d = d[:len(d) - 2].zfill(2)
            res.append(d)
        return '-'.join(res)