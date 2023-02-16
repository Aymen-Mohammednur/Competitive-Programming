class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        counter = Counter(changed)
        output = []
        for i in sorted(counter.keys()):
            if i == 0:
                while(counter[i] >= 2):
                    output.append(i)
                    counter[i] -= 2
            while(i > 0 and counter[i] and counter[i*2]):
                output.append(i)
                counter[i] -= 1
                counter[i*2] -= 1
        return output if len(output) == len(changed) // 2 else []