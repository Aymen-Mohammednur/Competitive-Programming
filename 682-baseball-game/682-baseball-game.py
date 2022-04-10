class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = []
        for index, element in enumerate(ops):
            if element == "+":
                records.append(records[-1] + records[-2])
            elif element == "D":
                records.append(records[-1] * 2)
            elif element == "C":
                records.pop()
            else:
                records.append(int(element))
        return sum(records)